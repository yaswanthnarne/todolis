import json
import os

# Function to load tasks from a file
def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return []

# Function to save tasks to a file
def save_tasks(tasks, file_path):
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task.get('completed', False) else "Pending"
            print(f"{idx}. {task['title']} - Due: {task.get('due_date', 'N/A')} - Status: {status}")

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    due_date = input("Enter due date (optional): ")
    new_task = {'title': title, 'due_date': due_date, 'completed': False}
    tasks.append(new_task)
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_idx]['completed'] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to delete: ")) - 1
        del tasks[task_idx]
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

# Main function
def main():
    file_path = 'tasks.json'  # File to store tasks
    tasks = load_tasks(file_path)

    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Task as Completed\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks, file_path)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
