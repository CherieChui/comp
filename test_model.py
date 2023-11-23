
import unittest
from model import validate_date, validate_alarm

class TestModel(unittest.TestCase):

    def test_validate_date_valid(self):
        self.assertTrue(validate_date("2023-01-01"))

    def test_validate_date_invalid(self):
        self.assertFalse(validate_date("2023-13-01"))

    def test_validate_date_format(self):
        self.assertFalse(validate_date("01-01-2023"))

    def test_validate_alarm_valid(self):
        self.assertTrue(validate_alarm("2023-01-01 09:00"))

    def test_validate_alarm_invalid(self):
        self.assertFalse(validate_alarm("2023-01-01 25:00"))

    def test_validate_alarm_format(self):
        self.assertFalse(validate_alarm("01-01-2023 09:00"))

# More tests can be added here for the PIM class if necessary

if __name__ == '__main__':
    unittest.main()
