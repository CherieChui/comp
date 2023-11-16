from builtins import input
import os
from datetime import datetime
import json

class Task:
    def __init__(self, name, description, deadline):
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Name and Description must be of type string.")
        self.name = name
        self.description = description
        self.deadline = deadline
        self.task_dict = {"name": self.name, "description": self.description, "deadline": self.deadline}

class TaskManager:
    def __init__(self, file_name):
        self.tasks = []
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            print("The file doesn't exist")
        
    def add_task(self, name, description, deadline):
        task = Task(name, description, deadline)
        self.tasks.append(task)
        if os.path.exists(self.file_name):
            self.write_task_to_file(task)
            print("Task added successfully!")
        
    def display_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(f"Task name: {task.task_dict['name']}\nDescription: {task.task_dict['description']}\nDeadline: {task.task_dict['deadline']}\n-----------------------")
                
    def write_task_to_file(self, task):
        with open(self.file_name, 'a') as file:
            file.write(json.dumps(task.task_dict))
            file.write("\n")

def validate_date(deadline_string): 
    try:
        datetime.strptime(deadline_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False 

file_name = input("Enter the existing file name: ")
task_manager = TaskManager(file_name)

if os.path.exists(file_name):
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
    while not validate_date(task_deadline):
        print("The input deadline is incorrect!")
        task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")

    task_manager.add_task(task_name, task_description, task_deadline)

    print("\nTask Added Content:")
    task_manager.display_tasks()
