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
            # TODO: Implement create todo item functionality
            print("Create a new todo item")
            
            item = input("Enter the todo item: ")
            Todo.create(item)
        elif choice == "2":
            print("Read a todo item")
            Todo.read()
            # TODO: Implement read todo item functionality
            
        elif choice == "3":
            # TODO: Implement update todo item functionality
            Todo.update(1, "Submit report") 
        elif choice == "4":
            # TODO: Implement list all todo items functionality
            Todo.read()
        elif choice == "5":
            # TODO: Implement delete todo item functionality
            Todo.delete(1)
            
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print(f"{Fore.RED} Invalid choice. Please try again.")

if __name__ == "__main__":
    main()