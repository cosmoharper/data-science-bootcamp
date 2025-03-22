# Starter Code:

"""

# Import functions from task_manager.task_utils package
None

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            None
        None
        None
        None
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

"""

# Solution: 

from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                title = input("Enter task title: ")
                desc = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                add_task(title, desc, due_date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                view_pending_tasks()
                index = int(input("Enter task index to mark complete: "))
                mark_task_as_complete(index)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Task Completion Progress: {progress:.1f}%")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()