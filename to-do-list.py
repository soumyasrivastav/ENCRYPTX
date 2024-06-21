# To-Do List Application

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. [{status}] {task['description']}")

def add_task(tasks):
    description = input("\nEnter the task description: ")
    tasks.append({'description': description, 'completed': False})
    print("Task added.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the number of the task to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
