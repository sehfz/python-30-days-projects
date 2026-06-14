import os
tasks = []
TODO_FILE="tasks.txt"
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
load_tasks()
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("choose (1-4): ")
    
    if choice=="1":
       task=input("Enter task: ")
       tasks.append(task)
       save_tasks()
       print("Task added!")
    
    elif choice=="2":
        if not tasks:
            print ("\nno tasks found! ")
        else:
            for i,number in enumerate(tasks, start=1):
                print(f"{i}. {number}")

        
    elif choice=="3":
        if not tasks:
            print ("\nNo tasks to delete!")
        else:
            for i,number in enumerate(tasks, start=1):
                print(f"{i}. {number}")
        delete_num=input("\nEnter task number to delete: ")
        try:
            delete_num=int(delete_num)
            if 1 <= delete_num <= len(tasks):
                    removed = tasks.pop(delete_num-1)
                    print(f"Removed: {removed}")
                    save_tasks()
            else :
                    print(" Invalid task number!")
        except ValueError:
                print("Please enter a valid number!")
    
    elif choice=="4":
        print("\nGoodbye! Tasks saved.")
        break
    else:
            print("Invalid choice! Please enter 1-4.")
    