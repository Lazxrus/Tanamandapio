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
        choice = input("Enter your choice: ")
        if choice == 1:
            add_tasks(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            task_completed(tasks)
        elif choice == 4:
            task_remove(tasks)
        elif choice == 5:
            print("Thank you for using our to-do app!")
            break


def add_tasks(tasks):
    description = input("Enter task name: ")
    task = {
        description: "description",
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("The to-do list is empty!")
    else:
        print("\n==== To-Do List ====")
        for index, task in enumerate(tasks, start=1):
            status = "COMPLETE" if status["completed"] else " "
            description = (f"{index}. [{status}]. {task['description']}")
        print("===========================")

def task_completed(tasks):
    print("\n==== To-Do List ====")
    for index, task in enumerate(tasks, start=1):
        status = "completed" if status ["completed"] else " "
        description = (f"{index}. [{status}], {task['description']}")
        print(description)
    while True:
        try:
            task_choice = int(input("Select the task you would like to complete(num): "))
            if 1 <= task_choice <= len(tasks):
                tasks[task_choice -1]["completed"] = True
                print(f"Task '{tasks[task_choice -1]}['description']' marked as completed!")
                break
            else:
                print("Please enter a valid task number!")
        except ValueError:
            print("Please enter a valid number!")

def task_remove(tasks):
    print("\n==== To-Do List ====")
    for index, task in enumerate(tasks, start=1):
        status = "completed" if status ["completed"] else " "
        description = (f"{index}. [{status}], {task['description']}")
        print(description)
    while True:
        try:
            task_choice = int(input("Select the task you would like to remove(num): "))
            if 1 <= task_choice <= len(tasks):
                removed_task = tasks.pop(task_choice - 1)
                print(f"Task '{removed_task['description']}' removed from the list!")
            break
        except ValueError:
            print("Please enter a valid number!")

def start(display_menu):
    print("Welcome, what would you like to do today?")