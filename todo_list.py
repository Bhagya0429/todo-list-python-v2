ef display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(task_list):
    task = input("Enter task: ")
    task_list.append(task)
    print("Task added!")

def view_tasks(task_list):
    if not task_list:
        print("No tasks added yet.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

def delete_task(task_list):
    view_tasks(task_list)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(task_list):
            removed = task_list.pop(task_num - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Enter choice (1-4): ")
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            delete_task(task_list)
        elif choice == "4":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


