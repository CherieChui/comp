
import unittest
from unittest.mock import patch
from view import check_int

class TestView(unittest.TestCase):

    def test_check_int_with_integer(self):
        self.assertTrue(check_int("5"))

    def test_check_int_with_non_integer(self):
        self.assertFalse(check_int("abc"))

    def test_check_int_with_empty_string(self):
        self.assertFalse(check_int(""))

# Testing Manage_PIR(pim) would require mocking inputs, which is more complex.

if __name__ == '__main__':
    unittest.main()
