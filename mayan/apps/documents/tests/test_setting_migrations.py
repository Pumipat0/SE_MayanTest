from django.test import override_settings

from mayan.apps.smart_settings.tests.mixins import SmartSettingTestMixin
from mayan.apps.testing.tests.base import BaseTestCase

from ..settings import (
    setting_document_file_page_image_cache_storage,
    setting_document_file_page_image_cache_storage_arguments,
    setting_document_file_storage_backend,
    setting_document_file_storage_backend_arguments,
    setting_document_version_page_image_cache_storage,
    setting_document_version_page_image_cache_storage_arguments,
    setting_recently_accessed_document_count,
    setting_recently_created_document_count,
)

from .literals import (
    TEST_DOCUMENTS_CACHE_STORAGE_BACKEND,
    TEST_DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS,
    TEST_DOCUMENTS_STORAGE_BACKEND, TEST_DOCUMENTS_STORAGE_BACKEND_ARGUMENTS,
    TEST_DOCUMENTS_RECENTLY_ACCESSED_COUNT,
    TEST_DOCUMENTS_RECENTLY_CREATED_COUNT
)


class DocumentSettingMigrationTestCase(SmartSettingTestMixin, BaseTestCase):
    @override_settings(DOCUMENTS_CACHE_STORAGE_BACKEND=TEST_DOCUMENTS_CACHE_STORAGE_BACKEND)
    def test_setting_document_file_page_image_cache_storage_0003(self):
        test_value = None
        self.test_setting = setting_document_file_page_image_cache_storage
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_document_file_page_image_cache_storage.value,
            TEST_DOCUMENTS_CACHE_STORAGE_BACKEND
        )

    @override_settings(DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS=TEST_DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS)
    def test_setting_document_file_page_image_cache_storage_arguments_0003(self):
        test_value = None
        self.test_setting = setting_document_file_page_image_cache_storage_arguments
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_document_file_page_image_cache_storage_arguments.value,
            TEST_DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS
        )

    @override_settings(DOCUMENTS_STORAGE_BACKEND=TEST_DOCUMENTS_STORAGE_BACKEND)
    def test_setting_document_file_storage_backend_0003(self):
        test_value = None
        self.test_setting = setting_document_file_storage_backend
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_document_file_storage_backend.value,
            TEST_DOCUMENTS_STORAGE_BACKEND
        )

    @override_settings(DOCUMENTS_STORAGE_BACKEND_ARGUMENTS=TEST_DOCUMENTS_STORAGE_BACKEND_ARGUMENTS)
    def test_setting_document_file_storage_backend_arguments_0003(self):
        test_value = None
        self.test_setting = setting_document_file_storage_backend_arguments
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_document_file_storage_backend_arguments.value,
            TEST_DOCUMENTS_STORAGE_BACKEND_ARGUMENTS
        )

    @override_settings(DOCUMENTS_CACHE_STORAGE_BACKEND=TEST_DOCUMENTS_CACHE_STORAGE_BACKEND)
    def test_setting_document_version_page_image_cache_storage_0003(self):
        test_value = None
        self.test_setting = setting_document_version_page_image_cache_storage
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_document_version_page_image_cache_storage.value,
            TEST_DOCUMENTS_CACHE_STORAGE_BACKEND
        )

    @override_settings(DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS=TEST_DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS)
    def test_setting_document_version_page_image_cache_storage_arguments_0003(self):
        test_value = None
        self.test_setting = setting_document_version_page_image_cache_storage_arguments
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_document_version_page_image_cache_storage_arguments.value,
            TEST_DOCUMENTS_CACHE_STORAGE_BACKEND_ARGUMENTS
        )

    @override_settings(DOCUMENTS_RECENT_ACCESS_COUNT=TEST_DOCUMENTS_RECENTLY_ACCESSED_COUNT)
    def test_setting_recently_accessed_document_count_0002(self):
        test_value = None
        self.test_setting = setting_recently_accessed_document_count
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_recently_accessed_document_count.value,
            TEST_DOCUMENTS_RECENTLY_ACCESSED_COUNT
        )

    @override_settings(DOCUMENTS_RECENT_ADDED_COUNT=TEST_DOCUMENTS_RECENTLY_CREATED_COUNT)
    def test_setting_recently_created_document_count_0002(self):
        test_value = None
        self.test_setting = setting_recently_created_document_count
        self.test_config_value = test_value
        self._create_test_config_file()

        self.assertEqual(
            setting_recently_created_document_count.value,
            TEST_DOCUMENTS_RECENTLY_CREATED_COUNT
        )
