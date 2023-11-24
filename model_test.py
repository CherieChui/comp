import unittest
from unittest.mock import patch, mock_open
from model import validate_date, validate_alarm, PIM

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

    def setUp(self):
        self.pim = PIM('test.pim')

    def test_init(self):
        # Test __init__ method
        self.assertEqual(self.pim.file_name, "test.pim")
        self.assertIsInstance(self.pim.data, dict)
        # More assertions can be added here

    def test_add_task(self):
        self.pim.add_task('Task 1', '2023-12-31')
        self.assertEqual(len(self.pim.data['tasks']), 1)
        self.assertEqual(self.pim.data['tasks'][0]['description'], 'Task 1')
        self.assertEqual(self.pim.data['tasks'][0]['deadline'], '2023-12-31')

    def test_add_event(self):
        # Test case 1: Adding an event with a description, starting time, and alarm
        self.pim.add_event('Event 1', '2023-12-31 10:00', True)
        self.assertEqual(len(self.pim.data['events']), 1)
        self.assertEqual(self.pim.data['events'][0]['description'], 'Event 1')
        self.assertEqual(self.pim.data['events'][0]['starting_time'], '2023-12-31 10:00')
        self.assertTrue(self.pim.data['events'][0]['alarm'])

    def test_add_contact(self):
        # Test case 1: Adding a contact with a name, address, and mobile number
        self.pim.add_contact('John Doe', '123 Main St', '123-456-7890')
        self.assertEqual(len(self.pim.data['contacts']), 1)
        self.assertEqual(self.pim.data['contacts'][0]['name'], 'John Doe')
        self.assertEqual(self.pim.data['contacts'][0]['address'], '123 Main St')
        self.assertEqual(self.pim.data['contacts'][0]['mobile_number'], '123-456-7890')


    def test_delete_record(self):
        # Test case 1: Deleting a task record
        self.pim.delete_record('tasks', 0)
        self.assertEqual(len(self.pim.data['tasks']), 0)

        # Test case 2: Deleting an event record
        self.pim.delete_record('events', 0)
        self.assertEqual(len(self.pim.data['events']), 0)

        # Test case 3: Deleting a contact record
        self.pim.delete_record('contacts', 0)
        self.assertEqual(len(self.pim.data['contacts']), 0)

        # Test case 5: Deleting a record with invalid record index
        self.pim.delete_record('tasks', 10)
        self.assertEqual(len(self.pim.data['tasks']), 0)

    def test_check_int(self):
        # Test check_int method
        result1 = self.pim.check_int("123")
        self.assertTrue(result1)

    def test_check_invalid_int(self):
        # Test check_int method
        result = self.pim.check_int("abc")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
