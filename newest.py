from datetime import datetime, timedelta
import os
import json

class Event:
    def __init__(self, description, start_time, alarm):
        self.description = description
        self.start_time = start_time
        self.alarm = alarm
        self.event_dict = {"type": "event", "description": self.description, "start_time": str(self.start_time), "alarm": str(self.alarm)}

class Task:
    def __init__(self, name, description, deadline):
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Name and Description must be of type string.")
        self.name = name
        self.description = description
        self.deadline = deadline
        self.task_dict = {"type": "task", "name": self.name, "description": self.description, "deadline": self.deadline}

class Manager:
    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            print("The file doesn't exist")

    def add_event(self, description, start_time, alarm):
        event = Event(description, start_time, alarm)
        self.write_to_file(event.event_dict)
        print("Event created!")

    def add_task(self, name, description, deadline):
        task = Task(name, description, deadline)
        self.write_to_file(task.task_dict)
        print("Task added successfully!")

    def write_to_file(self, item_dict):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'a') as file:
                file.write(json.dumps(item_dict))
                file.write("\n")

def validate_date(deadline_string): 
    try:
        datetime.strptime(deadline_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False 

file_name = input("Enter the existing file name: ")
manager = Manager(file_name)

if os.path.exists(file_name):
    # Add task
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
    while not validate_date(task_deadline):
        print("The input deadline is incorrect!")
        task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
    manager.add_task(task_name, task_description, task_deadline)
    with open(file_name, 'a') as file:
        file.write("----- Tasks Ends and Events Start -----\n")

    # Add event
    event_description = input("Enter event description: ")
    start_time_str = input("Enter event start time (YYYY-MM-DD HH:MM): ")
    while True:
        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid input for start time. Please enter a valid date and time in the format 'YYYY-MM-DD HH:MM'.")
    alarm_str = input("Enter event alarm (in minutes before start time): ")
    while True:
        try:
            alarm = timedelta(minutes=int(alarm_str))
            break
        except ValueError:
            print("Invalid input for alarm. Please enter a valid integer.")
    manager.add_event(event_description, start_time, alarm)
