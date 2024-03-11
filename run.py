import datetime
import todo
from colorama import init, Fore

def main():
    init()  # Initialize colorama
    Todo = todo.Todo()
    while True:
        print(f"{Fore.GREEN} TODO Menu:")
        print("1. Create a new todo item")
        print("2. Read a todo item")
        print("3. Update a todo item")
        print("4. List all todo items")
        print("5. Delete a todo item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Create a new todo item")
            
            item_name = input("Enter the todo item title: ")
            desc = input("Enter the todo item description: ")
            timeStamp = datetime.datetime.now()
            progress = input("Enter the progress of the task: ")
            item = {
                "title": item_name,
                "description": desc,
                "time": timeStamp.isoformat(),
                "progress": progress
            }
            Todo.create(item)
        elif choice == "2":
            print("Read a todo item")
            Todo.read()
            
        elif choice == "3":
           choice = input("Enter the index of the todo item to update: ")
           new_title = input("Enter the new title: ")
           new_discription = input("Enter the new description: ")
           new_time = datetime.datetime.now()
           new_progress = input("Enter the new progress: ")
           Todo.update(int(choice), {
                "title": new_title,
                "description": new_discription,
                "time": new_time.isoformat(),
                "progress": new_progress
            }) 
        elif choice == "4":
            
            Todo.read()
        elif choice == "5":
            delete_choice = input("Enter the index of the todo item to delete: ")
            
            Todo.delete(int(delete_choice))
            
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print(f"{Fore.RED} Invalid choice. Please try again.")

if __name__ == "__main__":
    main()