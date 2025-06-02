 GNU nano 8.2              daily_reminder.py               Modified
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
<level"# Time-sensitivity condition 
if time_bound == "yes":
 message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Final output (must start with Reminder:)
print(f"{message}")
