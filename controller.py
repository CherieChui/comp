from model import PIM
from view import print_menu, print_error_message, print_success_message, print_record

def run():
    pim = PIM('pim_data.json')
    while True:
        print_menu()
        option = input("Enter your option in number form: ")
        
        if option == '1':
            description = input("Enter the task description: ")
            deadline = input("Enter the task deadline (format YYYY-MM-DD): ")
            pim.add_task(description, deadline)
            print_success_message("Task added successfully")

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
            delete_function()

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


if __name__ == "__main__":
    run()
