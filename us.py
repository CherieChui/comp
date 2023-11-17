
import os
import json
import datetime

class PIM:
    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(file_name):
            print("The file has already been created. Would you like to operate on it? (yes/no)")
            if input().lower() == 'yes':
                with open(file_name, 'r') as f:
                    self.data = json.load(f)
        else:
            self.data = {'tasks': [], 'events': [], 'contacts': []}

    def save_data(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f)

    def add_task(self):
        description = input("Enter the task description: ")
        deadline = input("Enter the task deadline (format YYYY-MM-DD): ")
        self.data['tasks'].append({'description': description, 'deadline': deadline})
        self.save_data()

    def add_event(self):
        description = input("Enter the event description: ")
        starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM:SS): ")
        alarm = input("Enter the event alarm time (format YYYY-MM-DD HH:MM:SS): ")
        self.data['events'].append({'description': description, 'starting_time': starting_time, 'alarm': alarm})
        self.save_data()

    def add_contact(self):
        name = input("Enter the contact name: ")
        address = input("Enter the contact address: ")
        mobile_number = input("Enter the contact mobile number: ")
        self.data['contacts'].append({'name': name, 'address': address, 'mobile_number': mobile_number})
        self.save_data()

    def list_records(self):
        print("Tasks:")
        for task in self.data['tasks']:
            print(task)
        print("Events:")
        for event in self.data['events']:
            print(event)
        print("Contacts:")
        for contact in self.data['contacts']:
            print(contact)

    def delete_record(self, record_type, record_index):
        if record_index < len(self.data[record_type]):
            del self.data[record_type][record_index]
            self.save_data()
        else:
            print("Invalid record index.")

    def update_record(self, record_type, record_index):
        if record_index < len(self.data[record_type]):
            if record_type == 'tasks':
                self.add_task()
            elif record_type == 'events':
                self.add_event()
            elif record_type == 'contacts':
                self.add_contact()
            del self.data[record_type][record_index]
            self.save_data()
        else:
            print("Invalid record index.")


# USAGE
while True:
    filename = input("Enter a filename: ")
    pim = PIM(filename)

    print("1. Add task\n2. Add event\n3. Add contact\n4. List records\n5. Delete record\n6. Update record\n7. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        pim.add_task()
    elif option == 2:
        pim.add_event()
    elif option == 3:
        pim.add_contact()
    elif option == 4:
        pim.list_records()
    elif option == 5:
        record_type = input("Enter record type (tasks/events/contacts): ")
        record_index = int(input("Enter record index: "))
        pim.delete_record(record_type, record_index)
    elif option == 6:
        record_type = input("Enter record type (tasks/events/contacts): ")
        record_index = int(input("Enter record index: "))
        pim.update_record(record_type, record_index)
    elif option == 7:
        break
    else:
        print("Invalid option.")
