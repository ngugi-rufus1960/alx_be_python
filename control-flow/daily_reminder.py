# Prompt for task details
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Provide customized reminder using match-case (Python 3.10+)
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Add urgency if time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print(reminder)
