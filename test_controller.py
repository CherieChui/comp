
import unittest
from unittest.mock import patch, mock_open
from controller import check_whether_file_exist, check_pim_files
import os

class TestController(unittest.TestCase):

    def test_check_whether_file_exist_with_existing_file(self):
        with patch('os.path.isfile', return_value=True):
            self.assertTrue(check_whether_file_exist("dummy_file.pim"))

    def test_check_whether_file_exist_with_non_existing_file(self):
        with patch('os.path.isfile', return_value=False):
            self.assertFalse(check_whether_file_exist("non_existent_file.pim"))

    def test_check_pim_files_with_pim_files(self):
        with patch('os.listdir', return_value=["file1.pim", "file2.pim"]):
            self.assertTrue(check_pim_files("/dummy/path"))

    def test_check_pim_files_without_pim_files(self):
        with patch('os.listdir', return_value=["file1.txt", "file2.doc"]):
            self.assertFalse(check_pim_files("/dummy/path"))

    def test_check_pim_files_with_invalid_path(self):
        with patch('os.listdir', side_effect=FileNotFoundError()):
            self.assertFalse(check_pim_files("/invalid/path"))

if __name__ == '__main__':
    unittest.main()
