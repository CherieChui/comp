import unittest
from model import PIM, validate_date, validate_alarm

class TestModel(unittest.TestCase):

    def test_validate_date(self): 
        self.assertTrue(validate_date('2023-11-23'))  # This is a valid date, so return True
        self.assertFalse(validate_date('2023-13-23')) # This is a invalid date, so return False

    def test_validate_alarm(self):
        self.assertTrue(validate_alarm('2023-11-23 16:30')) # This is a valid date and time, so return True
        self.assertFalse(validate_alarm('2023-11-23 25:30')) # This is a invalid date and time, so return True

    def test_PIM(self):
        pim = PIM('test.pim')
        pim.data = {'tasks': [], 'events': [], 'contacts': []}
        self.assertEqual(pim.data, {'tasks': [], 'events': [], 'contacts': []})

        pim.add_task('Test task', '2023-11-23')
        self.assertEqual(pim.data['tasks'][0], {'description': 'Test task', 'deadline': '2023-11-23'})

        pim.add_event('Test event', '2023-11-23 16:30', '2023-11-23 15:30')
        self.assertEqual(pim.data['events'][0], {'description': 'Test event', 'starting_time': '2023-11-23 16:30', 'alarm': '2023-11-23 15:30'})

        pim.add_contact('Test contact', 'Test address', '1234567890')
        self.assertEqual(pim.data['contacts'][0], {'name': 'Test contact', 'address': 'Test address', 'mobile_number': '1234567890'})

        pim.delete_record('tasks', 0)
        self.assertEqual(pim.data['tasks'], [])

        pim.update_record('events', 0, description='Updated event')
        self.assertEqual(pim.data['events'][0]['description'], 'Updated event')

        result = pim.find_by_name('contacts', 'Test contact')
        self.assertEqual(result, {'name': 'Test contact', 'address': 'Test address', 'mobile_number': '1234567890'})

if __name__ == '__main__':
        unittest.main()
