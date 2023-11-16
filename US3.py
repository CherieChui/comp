import re
from datetime import datetime

# set parameters to task
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

# Create tasks
task_manager = TaskManager()
task_name = input("Enter the task name: ")
task_description = input("Enter the task description: ")
task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
while validate_date(task_deadline) != True:
    print("The input deadline is incorrect!")
    task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")

# add input content to the task
task_manager.add_task(task_name,task_description,task_deadline)
# Display tasks
print("")
print("Task Added Content:")
task_manager.display_tasks()



