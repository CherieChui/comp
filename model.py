# Filename: model.py

import os
import json
from datetime import datetime


# test if the input deadline is valid
def validate_date(time_string): 
    try:
        datetime.strptime(time_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_alarm(time_string): 
    try:
        datetime.strptime(time_string, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False


class PIM:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = {'tasks': [], 'events': [], 'contacts': []}
        if os.path.exists(file_name):
            self.status = False
            with open(file_name, 'r') as f:  # Load the file
                self.data = json.load(f)  # Update self.data with the content of the file
        else:
            with open(file_name, 'w') as f:  # Create the file
                json.dump(self.data, f)
            self.status = True
            
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

    def list_records(self, record_type=None, name=None):
        if record_type and name:  # If both record_type and name are provided
            for record in self.data[record_type]:
                if record_type == 'tasks' and record['description'] == name:
                    print( record)
                elif record_type == 'events' and record['description'] == name:
                    print(record)
                elif record_type == 'contacts' and record['name'] == name:
                    print(record)
        elif record_type:  # If only record_type is provided
            if self.data[record_type]:  # If list is not empty
                print(f"{record_type.capitalize()}:")
                for record in self.data[record_type]:
                    print(record)
            else:
                print("No record found.")
        else:  # If no parameters are provided
            if self.data['tasks'] or self.data['events'] or self.data['contacts']:  # If any list is not empty
                print("Tasks:")
                for task in self.data['tasks']:
                    print(task)
                print("Events:")
                for event in self.data['events']:
                    print(event)
                print("Contacts:")
                for contact in self.data['contacts']:
                    print(contact)
            else:
                print("No record found.")

    def delete_record(self, record_type, record_index):
        # Check if the record_type is valid
        if record_type not in ['tasks', 'events', 'contacts']:
            print("Invalid record type.")
            return
        # Check if the record_index is valid
        if not isinstance(record_index, int) or record_index < 0 or record_index >= len(self.data[record_type]):
            print("Invalid record index.")
            return
        del self.data[record_type][record_index]
        self.save_data()
       # Add success message

    def update_record(self, record_type, record_index, description=None, deadline=None, starting_time=None, alarm=None, name=None, address=None, mobile_number=None):
        # Check if the record_type is valid
        if record_type not in ['tasks', 'events', 'contacts']:
            print("Invalid record type.")
            return
        # Check if the record_index is valid
        if not isinstance(record_index, int) or record_index < 0 or record_index >= len(self.data[record_type]):
            print("Invalid record index.")
            return
        if record_type == 'tasks':
            self.data[record_type][record_index] = {'description': description, 'deadline': deadline}
        elif record_type == 'events':
            self.data[record_type][record_index] = {'description': description, 'starting_time': starting_time, 'alarm': alarm}
        elif record_type == 'contacts':
            self.data[record_type][record_index] = {'name': name, 'address': address, 'mobile_number': mobile_number}
        self.save_data()

    def find_by_name(self, record_type, name):
        # Check if the record_type is valid
        if record_type not in ['tasks', 'events', 'contacts']:
            print("Invalid record type.")
            return
        for record in self.data[record_type]:
            if record_type == 'tasks' and record['description'] == name:
                return record
            elif record_type == 'events' and record['description'] == name:
                return record
            elif record_type == 'contacts' and record['name'] == name:
                return record
        print("No record found with the provided name.")
        return None

    def check_int(self, number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def delete_function(self,selection):
        while True: 
            if selection == '1':
                record_type = input("Enter record type (tasks/events/contacts): ").lower()
                if record_type not in ['tasks', 'events', 'contacts']:
                    print("Invalid record type.")
                    continue
                self.list_records(record_type)
                record_index = input("Enter record index ( starting from 0 ): ")
                if not self.check_int(record_index):
                    print("Invalid record index.")
                    continue
                record_index = int(record_index)
                self.delete_record(record_type, record_index)
                print("Content deleted Successfully")
                print("-----------------------------------------")
                return
            
            elif selection == '2':
                print("---Files---")
                # Assuming you want to print all files in the current directory
                for file_name in os.listdir(os.getcwd()):
                    if file_name.endswith(".pim"):
                        print(file_name)
                file_name = input("Please choose the file you want to delete(without '.pim'): ")
                file_path = os.getcwd() + '/' + file_name + '.pim'
                if os.path.exists(file_path):
                    # Delete the file
                    os.remove(file_path)
                    print("File deleted successfully.")
                    print("-----------------------------------------")
                    return
                    
                else:
                    print("File does not exist.")
                    print("-----------------------------------------")

                return
            elif selection == '3':
                return
                
