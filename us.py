import os
import json
import datetime

class PIM:
    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {'tasks': [], 'events': [], 'contacts': []}

    def save_data(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f)

    def add_task(self, description, deadline):
        self.data['tasks'].append({'description': description, 'deadline': deadline})
        self.save_data()

    def add_event(self, description, starting_time, alarm):
        self.data['events'].append({'description': description, 'starting_time': starting_time, 'alarm': alarm})
        self.save_data()

    def add_contact(self, name, address, mobile_number):
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

    def update_record(self, record_type, record_index, description=None, deadline=None, starting_time=None, alarm=None, name=None, address=None, mobile_number=None):
        if record_index < len(self.data[record_type]):
            if record_type == 'tasks':
                self.data[record_type][record_index] = {'description': description, 'deadline': deadline}
            elif record_type == 'events':
                self.data[record_type][record_index] = {'description': description, 'starting_time': starting_time, 'alarm': alarm}
            elif record_type == 'contacts':
                self.data[record_type][record_index] = {'name': name, 'address': address, 'mobile_number': mobile_number}
            self.save_data()
        else:
            print("Invalid record index.")

    def find_by_name(self, record_type, name):
        for record in self.data[record_type]:
            if record_type == 'tasks' and record['description'] == name:
                return record
            elif record_type == 'events' and record['description'] == name:
                return record
            elif record_type == 'contacts' and record['name'] == name:
                return record
        return None

# USAGE
while True:
    filename = input("Enter a filename: ")
    pim = PIM(filename)

    print("1. Add task\n2. Add event\n3. Add contact\n4. List records\n5. Delete record\n6. Update record\n7. Find record\n8. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        description = input("Enter the task description: ")
        deadline = input("Enter the task deadline (format YYYY-MM-DD): ")
        pim.add_task(description, deadline)
    elif option == 2:
        description = input("Enter the event description: ")
        starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM:SS): ")
        alarm = input("Enter the event alarm time (format YYYY-MM-DD HH:MM:SS): ")
        pim.add_event(description, starting_time, alarm)
    elif option == 3:
        name = input("Enter the contact name: ")
        address = input("Enter the contact address: ")
        mobile_number = input("Enter the contact mobile number: ")
        pim.add_contact(name, address, mobile_number)
    elif option == 4:
        pim.list_records()
    elif option == 5:
        record_type = input("Enter record type (tasks/events/contacts): ")
        record_index = int(input("Enter record index: "))
        pim.delete_record(record_type, record_index)
    elif option == 6:
        record_type = input("Enter record type (tasks/events/contacts): ")
        record_index = int(input("Enter record index: "))
        if record_type == 'tasks':
            description = input("Enter the task description: ")
            deadline = input("Enter the task deadline (format YYYY-MM-DD): ")
            pim.update_record(record_type, record_index, description, deadline)
        elif record_type == 'events':
            description = input("Enter the event description: ")
            starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM:SS): ")
            alarm = input("Enter the event alarm time (format YYYY-MM-DD HH:MM:SS): ")
            pim.update_record(record_type, record_index, description, starting_time, alarm)
        elif record_type == 'contacts':
            name = input("Enter the contact name: ")
            address = input("Enter the contact address: ")
            mobile_number = input("Enter the contact mobile number: ")
            pim.update_record(record_type, record_index, description=None, starting_time=None, alarm=None, name=name, address=address, mobile_number=mobile_number)
    elif option == 7:
        record_type = input("Enter record type (tasks/events/contacts): ")
        name = input("Enter the name: ")
        print(pim.find_by_name(record_type, name))
    elif option == 8:
        break
    else:
        print("Invalid option.")
