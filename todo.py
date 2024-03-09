from colorama import Fore, Style

class Todo:
    def __init__(self):
        self.todos = []

    def create(self, item):
        self.todos.append(item)
        print(f"{Fore.GREEN}Todo item '{item}' created successfully!{Style.RESET_ALL}")

    def read(self):
        if not self.todos:
            print(f"{Fore.YELLOW}No todo items found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Todo items:{Style.RESET_ALL}")
            for i, item in enumerate(self.todos, start=1):
                print(f"{i}. {item}")

    def update(self, index, new_item):
        if index < 1 or index > len(self.todos):
            print(f"{Fore.RED}Invalid index.{Style.RESET_ALL}")
        else:
            self.todos[index - 1] = new_item
            print(f"{Fore.GREEN}Todo item at index {index} updated successfully!{Style.RESET_ALL}")

    def delete(self, index):
        if index < 1 or index > len(self.todos):
            print(f"{Fore.RED}Invalid index.{Style.RESET_ALL}")
        else:
            deleted_item = self.todos.pop(index - 1)
            print(f"{Fore.GREEN}Todo item '{deleted_item}' at index {index} deleted successfully!{Style.RESET_ALL}")
def main():
    print("This is the main function")
if __name__ == "__main__":
    main()
# Example usage
""" todo = Todo()
todo.create("Buy groceries")
todo.create("Finish coding project")
todo.read()
todo.update(2, "Submit report")
todo.delete(1)
todo.read() """