import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

try:
    from python_magic import magic
    USE_PYTHON_MAGIC = True
except:
    import mimetypes
    mimetypes.init()
    USE_PYTHON_MAGIC = False
    
    
#http://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
def copyfile(source, dest, buffer_size=1024 * 1024):
    """
    Copy a file from source to dest. source and dest
    can either be strings or any object with a read or
    write method, like StringIO for example.
    """
    if not hasattr(source, 'read'):
        source = open(source, 'rb')
    if not hasattr(dest, 'write'):
        dest = open(dest, 'wb')

    while 1:
        copy_buffer = source.read(buffer_size)
        if copy_buffer:
            dest.write(copy_buffer)
        else:
            break

    source.close()
    dest.close()


def _lazy_load(fn):
    _cached = []

    def _decorated():
        if not _cached:
            _cached.append(fn())
        return _cached[0]
    return _decorated

    
@_lazy_load
def load_backend():
    from converter.conf.settings import GRAPHICS_BACKEND as backend_name

    try:
        module = import_module('.base', 'converter.backends.%s' % backend_name)
        import warnings
        warnings.warn(
            "Short names for CONVERTER_BACKEND are deprecated; prepend with 'converter.backends.'",
            PendingDeprecationWarning
        )
        return module
    except ImportError, e:
        # Look for a fully qualified converter backend name
        try:
            return import_module('.base', backend_name)
        except ImportError, e_user:
            # The converter backend wasn't found. Display a helpful error message
            # listing all possible (built-in) converter backends.
            backend_dir = os.path.join(os.path.dirname(__file__), 'backends')
            try:
                available_backends = [f for f in os.listdir(backend_dir)
                        if os.path.isdir(os.path.join(backend_dir, f))
                        and not f.startswith('.')]
            except EnvironmentError:
                available_backends = []
            available_backends.sort()
            if backend_name not in available_backends:
                error_msg = ("%r isn't an available converter backend. \n" +
                    "Try using converter.backends.XXX, where XXX is one of:\n    %s\n" +
                    "Error was: %s") % \
                    (backend_name, ", ".join(map(repr, available_backends)), e_user)
                raise ImproperlyConfigured(error_msg)
            else:
                raise # If there's some other error, this must be an error in Mayan itself.


def get_mimetype(filepath):
    """
    Determine a file's mimetype by calling the system's libmagic
    library via python-magic or fallback to use python's mimetypes
    library
    """
    file_mimetype = u''
    file_mime_encoding = u''
    
    if USE_PYTHON_MAGIC:
        if os.path.exists(filepath):
            try:
                source = open(filepath, 'r')
                mime = magic.Magic(mime=True)
                file_mimetype = mime.from_buffer(source.read())
                source.seek(0)
                mime_encoding = magic.Magic(mime_encoding=True)
                file_mime_encoding = mime_encoding.from_buffer(source.read())
            finally:
                if source:
                    source.close()
    else:
        path, filename = os.path.split(filepath)
        file_mimetype, file_mime_encoding = mimetypes.guess_type(filename)
        
    return file_mimetype, file_mime_encoding

