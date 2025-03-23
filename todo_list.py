# ------------------------------
# 📌 Text-Based To-Do List App
# Author: [Your Name]
# Date: [Today's Date]
# Description:
# A simple command-line program that lets users add, view, complete, and delete tasks.
# ------------------------------

# We’ll use a list to store our tasks in memory
todo_list = []

# ------------------------------
# 📌 Function: Display Menu Options
# ------------------------------
def show_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# ------------------------------
# 📌 Function: View All Tasks
# ------------------------------
def view_tasks():
    print("\n📝 Your Tasks:")
    
    # If the list is empty, let the user know
    if not todo_list:
        print("   No tasks found.")
        return
    
    # Loop through tasks and display each one
    for index, task in enumerate(todo_list):
        status = "✅" if task['completed'] else "❌"
        print(f"   {index + 1}. [{status}] {task['title']}")

# ------------------------------
# 📌 Function: Add a New Task
# ------------------------------
def add_task():
    title = input("Enter the task description: ")
    
    # Each task is stored as a dictionary with 'title' and 'completed' fields
    new_task = {"title": title, "completed": False}
    
    # Append the new task to the list
    todo_list.append(new_task)
    print("✅ Task added!")

# ------------------------------
# 📌 Function: Mark a Task as Completed
# ------------------------------
def mark_completed():
    view_tasks()  # Show the current tasks first
    
    if not todo_list:
        return  # Exit if there are no tasks

    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]['completed'] = True
            print("✅ Task marked as completed!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# ------------------------------
# 📌 Function: Delete a Task
# ------------------------------
def delete_task():
    view_tasks()  # Show tasks before asking to delete

    if not todo_list:
        return

    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            deleted_task = todo_list.pop(task_number - 1)
            print(f"🗑️ Task '{deleted_task['title']}' deleted.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

# ------------------------------
# 🚀 Main Program Loop
# ------------------------------
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Goodbye!")
        break
    else:
        print("❗ Invalid option. Please choose 1-5.")
