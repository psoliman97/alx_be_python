Task = input("Enter your task: ")
Priority = input("priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        print(f"Reminder: '{Task}' is a {Priority} priority task")
    case "medium":
        print(f"Reminder: '{Task}' is a {Priority} priority task")
    case "low":
        print(f"Note: '{Task}' is a {Priority} priority task")
    
if Time_Bound == "yes":
    print("that requires immediate attention today!")
else:
    print("Consider completing it when you have free time.")
