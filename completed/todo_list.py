def display_menu():
    print("\n==== To-Do List Menu ====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Quit the application")
    print("==========================")

def get_user_choice():
    valid_choices = {'1', '2', '3', '4', '5'}
    while True:
        choice = input("Enter your choice(1-5): ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 to 5")

def main():
    tasks = []
    while True:
        display_menu()
        choice = get_user_choice() #more consistent input handling
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Thank you for using our to-do app!")
            break


def add_task(tasks):
    print("\n==== Add Task Menu ====")
    description = input("Enter task name: ")
    task = {
        'description': description,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    print("\n==== View Task Menu ====")
    if not tasks:
        print("The to-do list is empty!")
    else:
        print("\n==== To-Do List ====")
        for index, task in enumerate(tasks, start=1):
            status = "completed" if task["completed"] else "not completed"
            print(f"{index}. [{status}] {task['description']}")
        print("===========================")

def mark_task_completed(tasks):
    print("\n==== Tasks Completion Menu ====")
    if not tasks:
        print("The to-do list is empty!")
        return
    for index, task in enumerate(tasks, start=1):
        status = "completed" if task ["completed"] else "not completed"
        print(f"{index}. [{status}], {task['description']}")
    while True:
        try:
            task_choice = int(input("Select the task you would like to complete: "))
            if 1 <= task_choice <= len(tasks):
                tasks[task_choice - 1]["completed"] = True
                print(f"Task '{tasks[task_choice -1]['description']}' marked as completed!")
                break
            else:
                print("Please enter a valid task number!")
        except ValueError:
            print("Please enter a valid number!")

def remove_task(tasks):
    print("\n ===== Remove Tasks =====")
    if not tasks:
        print("The to-do list is empty!")
        return
    for index, task in enumerate(tasks, start=1):
        status = "completed" if task else "not completed"
        print(f"{index}. [{status}], {task['description']}")
    while True:
        try:
            task_choice = int(input("Select the task you would like to remove: "))
            if 1 <= task_choice <= len(tasks):
                removed_task = tasks.pop(task_choice - 1)
                print(f"Task '{removed_task['description']}' removed from the list!")
                break
            else:
                ("Please enter a valid task number!")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()