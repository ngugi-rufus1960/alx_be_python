# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case to handle task priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unrecognized priority level"

# Append time sensitivity message
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the final reminder
print(reminder)

Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

Reminder: 'Finish project report' is a high priority task that requires immediate attention today!

Enter your task: Read a book
Priority (high/medium/low): low
Is it time-bound? (yes/no): no

Note: 'Read a book' is a low priority task. Consider completing it when you have free time.

