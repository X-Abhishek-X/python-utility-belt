import sys
import json
import os
from datetime import datetime

# --- Configuration ---
TASKS_FILE = "tasks.json"

# --- Helper Functions ---

def load_tasks():
    """Reads tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Writes the list of tasks to the JSON file."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def get_next_id(tasks):
    """Calculates the next unique ID based on existing tasks."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def find_task_index(tasks, task_id):
    """Finds the index of a task by its ID."""
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return index
    return -1

def get_timestamp():
    """Returns current timestamp formatted as ISO string."""
    return datetime.now().isoformat()

# --- Command Implementations ---

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": get_timestamp(),
        "updatedAt": get_timestamp()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, description):
    tasks = load_tasks()
    index = find_task_index(tasks, task_id)
    
    if index != -1:
        tasks[index]["description"] = description
        tasks[index]["updatedAt"] = get_timestamp()
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    index = find_task_index(tasks, task_id)
    
    if index != -1:
        deleted_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def mark_status(task_id, status):
    tasks = load_tasks()
    index = find_task_index(tasks, task_id)
    
    if index != -1:
        tasks[index]["status"] = status
        tasks[index]["updatedAt"] = get_timestamp()
        save_tasks(tasks)
        print(f"Task {task_id} marked as {status}.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    print(f"{'ID':<5} {'Status':<15} {'Description'}")
    print("-" * 40)
    
    for task in tasks:
        if status_filter and task["status"] != status_filter:
            continue
        print(f"{task['id']:<5} {task['status']:<15} {task['description']}")

# --- Main CLI Handler ---

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]
    
    # Handle 'add' command
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Description required.")
        else:
            add_task(sys.argv[2])

    # Handle 'update' command
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: ID and new description required.")
        else:
            try:
                update_task(int(sys.argv[2]), sys.argv[3])
            except ValueError:
                print("Error: Task ID must be a number.")

    # Handle 'delete' command
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Task ID required.")
        else:
            try:
                delete_task(int(sys.argv[2]))
            except ValueError:
                print("Error: Task ID must be a number.")

    # Handle status changes
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Task ID required.")
        else:
            try:
                mark_status(int(sys.argv[2]), "in-progress")
            except ValueError:
                print("Error: Task ID must be a number.")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Task ID required.")
        else:
            try:
                mark_status(int(sys.argv[2]), "done")
            except ValueError:
                print("Error: Task ID must be a number.")

    # Handle 'list' command
    elif command == "list":
        if len(sys.argv) == 3:
            filter_choice = sys.argv[2]
            if filter_choice in ["done", "todo", "in-progress"]:
                list_tasks(filter_choice)
            else:
                print("Error: Invalid status filter. Use done, todo, or in-progress.")
        else:
            list_tasks()

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()