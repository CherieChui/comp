import re

class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, name, description, deadline):
        task = Task(name, description, deadline)
        self.tasks.append(task)
        print("Task added successfully!")
        
    def display_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print("Task name:", task.name)
                print("Description:", task.description)
                print("Deadline:", task.deadline)
                print("-----------------------")
        else:
            print("No tasks found!")

def validate_date(deadline_string):
    pattern = r"\d{4}-\d{2}-\d{2}"
    if re.match(pattern, deadline_string):
        return True
    else:
        return False   

# Add tasks
task_manager = TaskManager()
task_name = input("Enter the task name: ")
task_description = input("Enter the task description: ")

task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")
while validate_date(task_deadline) != True:
    print("The input deadline is incorrect!")
    task_deadline = input("Enter the deadline of task in form of YYYY-MM-DD: ")

task_manager.add_task(task_name,task_description,task_deadline)

# Display tasks
print("")
print("Task Added:")
task_manager.display_tasks()


