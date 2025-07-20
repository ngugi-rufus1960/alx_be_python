# daily_reminder.py

# Ask the user to enter the task description
task = input("Enter your task: ")

# Ask the user to specify the priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""

# Use match-case to handle different priority levels
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a high priority task. Try to address it soon."
    case "medium":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a medium priority task. Plan accordingly."
    case "low":
        if time_bound == "yes":
            reminder = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Note: '{task}' has an unknown priority level. Please review the input."

# Display the reminder
print("\n" + reminder)
