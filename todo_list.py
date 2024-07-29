# 1. Create a menu-driven console application

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
            task_complete(tasks)
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

def task_complete(tasks):
    print("\n==== To-Do List ====")
    print(tasks.index)
    while True:
        mark_task_complete = input("Which task would you like to mark as completed? Enter a number: ")
        if mark_task_complete in tasks:
            task_complete = True
        else:
            print("Please enter a valid choice")

def task_remove(tasks):
    


def app_exit():
    break

# 3. Use a list to store tasks
# 4. Each task should be a dictionary containing:
#    - Task description
#    - Completion status (True/False)
# 5. Implement input validation where necessary
# 6. Use functions to organize your code