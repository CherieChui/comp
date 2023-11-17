from datetime import datetime
from builtins import input
import os

# personal information----------------------------------------
class information:
    def __init__(self, name, contact, address):
        self.name = name
        self.contact = contact
        self.address = address

class InfoManage:
    def __init__(self):
        self.info = []
    def add_info(self, name, contact, address):
        Info = information(name, contact, address)
        self.info.append(Info)
    
    def display_data(self):
        if self.info:
            for Info in self.info:
                print("NAME: " + User_name + " | " + "ADDRESS: " + User_address + " | " + "CONTACT: " + User_contact)
#-------------------------------------------------------------


# Task information--------------------------------------------
class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        

# set functions to tasks
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, name, description, deadline):
        task = Task(name, description, deadline)
        self.tasks.append(task)
        print("Task added successfully!")
        
    def display_tasks(self):
        list = {}
        if self.tasks:
            for task in self.tasks:
                list[task_name] = task_description + ' , ' + task_deadline
                print(list)

# test if the input deadline is valid
    def validate_date(deadline_string): 
        try:
            datetime.strptime(deadline_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False
#-------------------------------------------------------------


# Create File-------------------------------------------------
def create_pir():
    file_name = input("Enter the file name for the new PIR: ")

    if os.path.exists(file_name):
        print(file_name + " file already exists.")
    else:
        try:
            with open(file_name, 'w') as file:
                print("New PIR created: " + file_name)
            with open(file_name, 'r') as file:
                pir_text = file.read()
                if pir_text:
                    print("PIR content:")
                    print(pir_text)
                else:
                    print("Empty PIR file.")
        except IOError:
            print("Error: Unable to create or open the PIR file.")
#----------------------------------------------------------------


# Menu
print("")
print("")
print("----------------------------------------------")
print("Welcome to the Personal Information Management")
print("----------------------------------------------")
print("Here are the menue for you to select from")
print("1. Create a new Personal Information record")
print("2. Manage PIR")
print("3. List spcific PIR")
choice = input("Please Enter your selection: ")
if choice == '1':
    create_pir()

    
    info_manage = InfoManage()
    User_name = input("Enter your name: ")
    User_address = input("Enter your address: ")
    User_contact = input("Enter your contact number: ")
    info_manage.add_info(User_name,User_address,User_contact)
    info_manage.display_data


if choice == '2':
    print("")
    print("-------------------------------")
    print("1. Add new Tasks")
    print("2. Modify Tasks")
    print("3. Add new Events")
    print("4. Modify Events")
    print("-------------------------------")
    selection = input("Please Enter your selection: ")
    if selection == '1':
        task_manager = TaskManager()
        task_name = input("Enter the task name: ")
        task_description = input("Enter the task description: ")
        task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
        while TaskManager.validate_date(task_deadline) != True:
            print("The input deadline is incorrect!")
            task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
        # add input content to the task
        task_manager.add_task(task_name,task_description,task_deadline)
        # Display tasks
        print("Task Added Content:")
        task_manager.display_tasks()


    