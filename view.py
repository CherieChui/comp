# Filename: view.py

from model import PIM, validate_date, validate_alarm
from datetime import datetime


# check if the input number is not int
def check_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def Manage_PIR(pim):
    while True:
        print("--------------------Menu----------------------")
        print("1. Add task\n2. Add event\n3. Add contact\n4. List records\n5. Delete record\n6. Update record\n7. Find record\n8. Go Back")
        option = input("Enter your option in number form: ")
        
        # All the other option selection logic goes here
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
            while validate_alarm(alarm) != True or datetime.strptime(alarm, "%Y-%m-%d %H:%M") >= datetime.strptime(starting_time, "%Y-%m-%d %H:%M"):
                print("Invalid Input or alarm time is not before the event starting time, please try again!")
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
            option = input("Enter your option: ")
            if not check_int(option):
                print("Invalid option.")
                continue
            option = int(option)
            if option == 1:
                pim.list_records()
            elif option == 2:
                record_type = input("Enter record type (tasks/events/contacts): ")
                if record_type not in ['tasks', 'events', 'contacts']:
                    print("Invalid record type.")
                    continue
                pim.list_records(record_type)
            elif option == 3:
                record_type = input("Enter record type (tasks/events/contacts): ")
                if record_type not in ['tasks', 'events', 'contacts']:
                    print("Invalid record type.")
                    continue
                name = input("Enter the name: ")
                pim.list_records(record_type, name)
            else:
                print("Invalid option.")
                continue

        elif option == '5':
                print("1. Delete one specific PIR")
                print("2. Delete a file")
                print("3. Go Back")
                selection = input("Please selection one option: ")
                if (selection == '1' or selection == '2' or selection == '3'):
                    pim.delete_function(selection)
                    if selection == '2':
                        return
                else: print("Invalid Input")
                
                
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
                while validate_date(deadline) != True:
                    print("Invalid Input, please try again!")
                    deadline = input("Enter the deadline (format YYYY-MM-DD): ")
                pim.update_record(record_type, record_index, description, deadline)
    
            elif record_type == 'events':
                description = input("Enter the event description: ")
                starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM): ")
                while validate_alarm(starting_time) != True:
                    print("Invalid Input, please try again!")
                    starting_time = input("Enter the event starting time (format YYYY-MM-DD HH:MM): ")
                alarm = input("Enter the event alarm time (format YYYY-MM-DD HH:MM): ")
                while validate_alarm(alarm) != True or datetime.strptime(alarm, "%Y-%m-%d %H:%M") >= datetime.strptime(starting_time, "%Y-%m-%d %H:%M"):
                    print("Invalid Input or alarm time is not before the event starting time, please try again!")
                    alarm = input("Enter the event alarm (format YYYY-MM-DD HH:MM): ")
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
            if record_type not in ['tasks', 'events', 'contacts']:
                print("Invalid record type.")
                continue
            name = input("Enter the name: ")
            print(pim.find_by_name(record_type, name))

        elif option == '8':
            return "back"
        else:
            print("Invalid input, Please try again")
