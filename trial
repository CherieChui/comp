from datetime import datetime, timedelta

class Event:
    def __init__(self, description, start_time, alarm):
        self.description = description
        self.start_time = start_time
        self.alarm = alarm

# Function to create a new event
def create_event():
    description = input("Enter event description: ")

    # Handle start time input with error handling and hints
    while True:
        start_time_str = input("Enter event start time (YYYY-MM-DD HH:MM): ")
        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid input for start time. Please enter a valid date and time in the format 'YYYY-MM-DD HH:MM'.")

    # Handle alarm input with error handling and hints
    while True:
        alarm_str = input("Enter event alarm (in minutes before start time): ")
        try:
            alarm = timedelta(minutes=int(alarm_str))
            break
        except ValueError:
            print("Invalid input for alarm. Please enter a valid integer.")

    # Create the event object
    event = Event(description, start_time, alarm)

    return event

# Example usage
event = create_event()
print("Event created:")
print("Description:", event.description)
print("Start Time:", event.start_time)
print("Alarm:", event.alarm)
