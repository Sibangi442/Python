import sys

def main():
    todo_list = {}

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View tasks by category")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            task = input("Enter the task description: ").strip()
            category = input("Enter the category (e.g., Work, Personal, Shopping): ").strip()
            if not category:
                category = "Uncategorized"
                
            if category not in todo_list:
                todo_list[category] = []
            todo_list[category].append({"task": task, "completed": False})
            print(f"Task '{task}' added to category '{category}'.")
            
        elif choice == '2':
            if not todo_list:
                print("Your to-do list is empty.")
            else:
                for category, tasks in todo_list.items():
                    print(f"\n[{category}]")
                    for idx, t in enumerate(tasks):
                        status = "[X]" if t["completed"] else "[ ]"
                        print(f"  {idx + 1}. {status} {t['task']}")
                        
        elif choice == '3':
            category = input("Enter the category to view: ").strip()
            if category in todo_list and todo_list[category]:
                print(f"\n[{category}]")
                for idx, t in enumerate(todo_list[category]):
                    status = "[X]" if t["completed"] else "[ ]"
                    print(f"  {idx + 1}. {status} {t['task']}")
            else:
                print(f"No tasks found in category '{category}'.")
                
        elif choice == '4':
            category = input("Enter the category of the task: ").strip()
            if category in todo_list and todo_list[category]:
                try:
                    task_num = int(input("Enter the task number to mark as completed: ").strip())
                    if 1 <= task_num <= len(todo_list[category]):
                        todo_list[category][task_num - 1]["completed"] = True
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print(f"No tasks found in category '{category}'.")

        elif choice == '5':
            category = input("Enter the category of the task: ").strip()
            if category in todo_list and todo_list[category]:
                try:
                    task_num = int(input("Enter the task number to delete: ").strip())
                    if 1 <= task_num <= len(todo_list[category]):
                        deleted_task = todo_list[category].pop(task_num - 1)
                        print(f"Task '{deleted_task['task']}' deleted.")
                        if not todo_list[category]:
                            del todo_list[category] # Remove category if it becomes empty
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print(f"No tasks found in category '{category}'.")
                
        elif choice == '6':
            print("Exiting To-Do List Manager. Goodbye!")
            sys.exit()
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
