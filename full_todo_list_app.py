import json
import os
from datetime import datetime

# Multi-user dictionary to store tasks per user
user_data = {}
current_user = None
data_file = 'todo_data.json'

# Load user data from file if it exists
if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        user_data = json.load(f)

# Authenticate user
def login():
    global current_user
    print("=== User Login ===")
    username = input("Username: ")
    password = input("Password: ")
    
    # For demo, simple password matching; in real apps, hash passwords
    if username in user_data:
        if user_data[username]['password'] == password:
            current_user = username
            print(f"Welcome back, {username}!")
        else:
            print("Invalid password.")
            exit()
    else:
        print("New user! Creating account.")
        user_data[username] = {"password": password, "tasks": []}
        current_user = username

# Save user data to file
def save_tasks():
    with open(data_file, 'w') as f:
        json.dump(user_data, f)

# View statistics
def show_stats():
    tasks = user_data[current_user]["tasks"]
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    print(f"Total tasks: {total} | Completed: {completed} | Pending: {pending}")

# Search tasks by keyword
def search_tasks():
    keyword = input("Enter keyword to search: ").lower()
    results = [t for t in user_data[current_user]["tasks"] if keyword in t['title'].lower()]
    if results:
        for i, t in enumerate(results, 1):
            print(f"{i}. [{t['due']}] {t['title']} - Priority: {t['priority']} - {'✅' if t['completed'] else '❌'}")
    else:
        print("No matching tasks found.")

# Add task
def add_task():
    title = input("Task: ")
    due = input("Due date (YYYY-MM-DD): ")
    priority = input("Priority (Low/Medium/High): ")
    task = {
        "title": title,
        "completed": False,
        "due": due,
        "priority": priority
    }
    user_data[current_user]["tasks"].append(task)
    print("Task added.")

# View all tasks
def view_tasks():
    tasks = user_data[current_user]["tasks"]
    if not tasks:
        print("No tasks found.")
    else:
        for idx, t in enumerate(tasks, 1):
            print(f"{idx}. [{t['due']}] {t['title']} - Priority: {t['priority']} - {'✅' if t['completed'] else '❌'}")

# Mark task as completed
def mark_task():
    view_tasks()
    try:
        task_num = int(input("Task number to mark as complete: "))
        tasks = user_data[current_user]["tasks"]
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print("Task marked complete.")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input.")

# Delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Task number to delete: "))
        tasks = user_data[current_user]["tasks"]
        if 0 < task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted: {deleted['title']}")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input.")

# GUI (optional integration placeholder)
def gui_notice():
    print("GUI version not included in CLI app. Try tkinter_gui.py for GUI.")

# Menu
def menu():
    while True:
        print("\n=== To-Do Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. View Statistics")
        print("7. Export to Excel")  # <-- new option
        print("8. Save & Exit")
        choice = input("Choose (1-8): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            search_tasks()
        elif choice == '6':
            show_stats()
        elif choice == '7':
            export_to_excel()  # <-- call new function
        elif choice == '8':
            save_tasks()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


import pandas as pd

def export_to_excel():
    tasks = user_data[current_user]["tasks"]

    if not tasks:
        print("No tasks to export.")
        return

    # Convert the task list (list of dicts) to a DataFrame
    df = pd.DataFrame(tasks)

    # Create a filename using the current user's name
    filename = f"{current_user}_todo_list.xlsx"

    # Export to Excel
    df.to_excel(filename, index=False)
    print(f"✅ Tasks exported to {filename}")


# Run the app
login()
menu()
