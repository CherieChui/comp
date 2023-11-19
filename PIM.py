import os
import json
from datetime import datetime
import sys


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
        self.data = {'tasks': [], 'events': [], 'contacts': []} # Move this line here
        if os.path.exists(file_name):
            print(f"The file {file_name} already exists.")
            self.status = False
            with open(file_name, 'r') as f:  # Load the file
                self.data = json.load(f)  # Update self.data with the content of the file
        else:
            with open(file_name, 'w') as f:  # Create the file
                json.dump(self.data, f)
            self.status = True
        
    # This function save input data in the txt file
    def save_data(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f)

    # add task function to ask user to 
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


# check if the input number is not int
def check_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


# Manage function to PIR----------------------------------------------------------------------------------------------------------------------
def Manage_PIR():
    while True:
        print("--------------------Menu----------------------")
        print("1. Add task\n2. Add event\n3. Add contact\n4. List records\n5. Delete record\n6. Update record\n7. Find record\n8. Go Back")
        option = input("Enter your option in number form: ")
            
        if option == '1':
            description = input("Enter the task description: ")
            deadline = input("Enter the task deadline (format YYYY-MM-DD): ")
            while validate_date(deadline) != True:
                    print("Invalid Input, please try again!")
                    deadline = input("Enter the deadline (format YYYY-MM-DD): ")
            pim.add_task(description, deadline)
            print("Task added Successfully")

        elif option == '2':
            description = input("Enter the event description: ")
            starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM): ")
            while validate_alarm(starting_time) != True:
                    print("Invalid Input, please try again!")
                    starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM): ")
                    
            alarm = input("Enter the event alarm time (format YYYY-MM-DD HH:MM): ")
            while validate_alarm(alarm) != True:
                    print("Invalid Input, please try again!")
                    alarm = input("Enter the event alarm (format YYYY-MM-DD HH:MM): ")
            pim.add_event(description, starting_time, alarm)
            print("Event added Successfully")

        elif option == '3':
            name = input("Enter the contact name: ")
            address = input("Enter the contact address: ")
            mobile_number = input("Enter the contact mobile number: ")
            while check_int(mobile_number) != True:
                print("Invalid Input, Please try again")
                mobile_number = input("Enter the contact mobile number: ")
            pim.add_contact(name, address, mobile_number)
            print("Contact added Successfully")
            
        elif option == '4':
            print("1. List all records\n2. List specific record type\n3. List specific record type with name")
            option = int(input("Enter your option: "))
            if option == 1:
                pim.list_records()
            elif option == 2:
                record_type = input("Enter record type (tasks/events/contacts): ")
                pim.list_records(record_type)
            elif option == 3:
                record_type = input("Enter record type (tasks/events/contacts): ")
                name = input("Enter the name: ")
                pim.list_records(record_type, name)
            else:
                print("Invalid option.")
                
        elif option == '5':
            record_type = input("Enter record type (tasks/events/contacts): ").lower()
            if record_type not in ['tasks', 'events', 'contacts']:
                print("Invalid record type.")
                continue
            pim.list_records(record_type)
            record_index = input("Enter record index ( starting from 0 ): ")
            if not check_int(record_index):
                print("Invalid record index.")
                continue
            record_index = int(record_index)
            pim.delete_record(record_type, record_index)
            print("Content deleted Successfully")

        elif option == '6':
            record_type = input("Enter record type (tasks/events/contacts): ").lower()
            if record_type not in ['tasks', 'events', 'contacts']:
                print("Invalid record type.")
                continue
            pim.list_records(record_type)
            record_index = input("Enter record index: ")
            
            if not check_int(record_index):
                print("Invalid record index.")
                continue
            record_index = int(record_index)

            if record_type == 'tasks':
                description = input("Enter the task description: ")
                deadline = input("Enter the task deadline (format YYYY-MM-DD): ")
                pim.update_record(record_type, record_index, description, deadline)
    
            elif record_type == 'events':
                description = input("Enter the event description: ")
                starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM): ")
                alarm = input("Enter the event alarm time (format YYYY-MM-DD HH:MM): ")
                pim.update_record(record_type, record_index, description, starting_time, alarm)

            elif record_type == 'contacts':
                name = input("Enter the contact name: ")
                address = input("Enter the contact address: ")
                mobile_number = input("Enter the contact mobile number: ")
                while check_int(mobile_number) != True:
                    print("Invalid Input, Please try again")
                    mobile_number = input("Enter the contact mobile number: ")
                pim.update_record(record_type, record_index, description=None, starting_time=None, alarm=None, name=name, address=address, mobile_number=mobile_number)
                print("Content updated Successfully")

        elif option == '7':
            record_type = input("Enter record type (tasks/events/contacts): ")
            name = input("Enter the name: ")
            print(pim.find_by_name(record_type, name))

        elif option == '8':
            return "back"
        else:
            print("Invalid input, Please try again")


# Print out all the files----------------------------------------------------------------------------------------------------------------------
def print_all_files():
    print("------------ALL FILES------------")
    txt_files = [file_name for file_name in os.listdir(current_path) if file_name.endswith('.pim')]

    if not txt_files:  # Check if the list is empty
        print("No text files found. Returning to main menu.")
        return False  # Return False if no files found

    for file_name in txt_files:
        file_path = current_path + '/' + file_name
        with open(file_path, 'r') as file:
            file_content = file.read()
        print(file_name)

    return True  # Return True if files are found

# check whether input file exists----------------------------------------------------------------------------------------------------------------------
def check_whether_file_exist(file_path):
    return os.path.exists(file_path)
    
# USAGE
current_path = os.getcwd()

print("")
print("----------------------------------------------")
print("Welcome to the Personal Information Management")
print("----------------------------------------------")
while True:
    print("-------Menu-------")
    print("1. Create a new PIR")
    print("2. Manage the PIR")
    print("3. Terminate the System")
    selection = input("Please choose one of the options above: ")
    if selection == '1':
        file = input("Please Enter a File Name (without '.pim'): ")
        filename = file + '.pim'
        file_path = current_path + '/' + filename
        while check_whether_file_exist(file_path) == True:
            print("The file already exists, please try again")
            file = input("Please Select one File Above (without '.pim'): ")
            filename = file + '.pim'
            file_path = current_path + '/' + filename
            
        pim = PIM(filename)
        if Manage_PIR() == "back":
            continue

    if selection == '2':
        while print_all_files():
            file = input("Please Select one File Above (without '.pim'): ")
            filename = file + '.pim'
            file_path = current_path + '/' + filename
            while check_whether_file_exist(file_path) != True:
                print("The file does not exist, please try again")
                file = input("Please Select one File Above (without '.pim'): ")
                filename = file + '.pim'
                file_path = current_path + '/' + filename
                
            pim = PIM(filename)
            if Manage_PIR() == "back":
                break
    elif selection == '3':
        sys.exit()

    else:
        print("Invalid input, Please try again")
