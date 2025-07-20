# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = ""

# Match case based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

# Add time sensitivity response
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority in ("medium", "low"):
        reminder += ". Consider completing it when you have free time."
    elif priority == "high":
        reminder += "."

# Display final message
print(reminder)
