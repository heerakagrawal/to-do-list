#to-do list application
tasks = []

def addTask(): #to add tasks in the list.
    task = input("Please Enter a Task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks(): #to list all the tasks present in the lsit.
    if not tasks:
        print("there are no tasks currently.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():#to delete specific task from the list.
    listTasks()
    try:
        taskToDelete = int(input("Choose the number of the task you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
        else:
            print(f"task #{taskToDelete} was not found.")
    except:
        print("Invalid Input.")

def markTask(): #to mark tasks as completed.
    listTasks()
    try:
        taskToMark = int(input("Choose the number of the task you want to mark: "))
        if taskToMark >= 0 and taskToMark < len(tasks):
            tasks[taskToMark] += "(Completed)"
        else:
            print(f"task #{taskToMark} was not found.")
    except:
        print("Invalid Input.")


if __name__ == "__main__":#main block
    print("Welcome to the to-do list app!")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.Mark a task")
        print("4.List all tasks")
        print("5.Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            markTask()
        elif(choice == "4"):
            listTasks()
        elif(choice == "5"):
            break
        else:
            print("Invalid input.")
