
import unittest
from unittest.mock import patch, MagicMock
from controller import check_whether_file_exist, check_pim_files, print_all_files, main

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

    def test_print_all_files_with_pim_files(self):
        with patch('os.listdir', return_value=["file1.pim", "file2.pim"]):
            with patch('builtins.print') as mock_print:
                print_all_files()
                mock_print.assert_called()

    def test_main_with_valid_selection(self):
        with patch('builtins.input', return_value='1'), patch('os.getcwd', return_value='/dummy/path'), patch('controller.print_all_files'):
            main('1')

# Additional tests can be added to cover more scenarios in the main function

if __name__ == '__main__':
    unittest.main()
