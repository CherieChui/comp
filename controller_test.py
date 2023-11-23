import unittest
from unittest.mock import patch
from controller import check_whether_file_exist, check_pim_files, print_all_files

class TestController(unittest.TestCase):

    @patch('os.path.isfile')
    def test_check_whether_file_exist(self, mock_isfile):
        mock_isfile.return_value = True
        self.assertTrue(check_whether_file_exist('test.pim'))

    @patch('os.listdir')
    def test_check_pim_files(self, mock_listdir):
        mock_listdir.return_value = ['test.pim']
        self.assertFalse(check_pim_files('/path'))

    @patch('os.listdir')
    def test_print_all_files(self, mock_listdir):
        mock_listdir.return_value = ['test.pim']
        self.assertTrue(print_all_files())  

if __name__ == '__main__':
    unittest.main()
