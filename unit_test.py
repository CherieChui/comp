import unittest
import os
from PIM import PIM, validate_date, validate_alarm, check_int

class TestPIM(unittest.TestCase):
    def setUp(self):
        self.pim = PIM("test_file.json")

    def tearDown(self):
        os.remove("test_file.json")

    # Test the validate_date function
    def test_validate_date(self):
        self.assertEqual(validate_date("2023-11-18"), True)
        self.assertEqual(validate_date("invalid_date"), False)

    # Test the validate_alarm function
    def test_validate_alarm(self):
        self.assertEqual(validate_alarm("2023-11-18 15:30"), True)
        self.assertEqual(validate_alarm("invalid_alarm"), False)

    # Test the check_int function
    def test_check_int(self):
        self.assertEqual(check_int("123"), True)
        self.assertEqual(check_int("abc"), False)

    # Test the PIM class
    def test_add_task(self):
        self.pim.add_task("Test task", "2023-11-18")
        self.assertEqual(len(self.pim.data['tasks']), 1)

    def test_add_event(self):
        self.pim.add_event("Test event", "2023-11-18 15:30", "2023-11-18 15:00")
        self.assertEqual(len(self.pim.data['events']), 1)

    def test_add_contact(self):
        self.pim.add_contact("Test name", "Test address", "1234567890")
        self.assertEqual(len(self.pim.data['contacts']), 1)

    def test_delete_record(self):
        self.pim.add_task("Test task", "2023-11-18")
        self.pim.delete_record('tasks', 0)
        self.assertEqual(len(self.pim.data['tasks']), 0)

    def test_update_record(self):
        self.pim.add_task("Test task", "2023-11-18")
        self.pim.update_record('tasks', 0, "Updated task", "2023-11-19")
        self.assertEqual(self.pim.data['tasks'][0]['description'], "Updated task")

    def test_find_by_name(self):
        self.pim.add_contact("Test name", "Test address", "1234567890")
        result = self.pim.find_by_name('contacts', "Test name")
        self.assertEqual(result['name'], "Test name")


if __name__ == '__main__':
    unittest.main()
