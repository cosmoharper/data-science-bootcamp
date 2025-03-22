from datetime import datetime
# Starter Code:

"""

# Import validation functions
None

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    None
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    None
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    None

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    None
    return progress

"""

# Solution 1: define functions for adding a task, marking a task as complete, viewing pending tasks, and calculating progress, making sure to consider validation

from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    # Validate all inputs
    validated_title = validate_task_title(title)
    validated_desc = validate_task_description(description)
    validated_date = validate_due_date(due_date)

    task = {
        "title": validated_title,
        "description": validated_desc,
        "due_date": validated_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if not tasks or index < 0 or index >= len(tasks):
        raise ValueError("Invalid task index")
    if tasks[index]["completed"]:
        raise ValueError("Task is already completed")
    tasks[index]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return

    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks!")
        return

    print("\nPending Tasks:")
    for i, task in enumerate(pending_tasks):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}\n")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100
    return progress