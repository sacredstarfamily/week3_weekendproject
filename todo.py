from colorama import Fore, Style
import json

class Todo:
    def __init__(self):
        self.todos = []
    def __save_to_file(self, filename):
            with open(filename, 'w') as file:
                json.dump(self.todos, file)

    def __load_from_file(self, filename):
            with open(filename, 'r') as file:
                self.todos = json.load(file)
    def create(self, item):
        
        self.todos.append(item)
        self.__save_to_file("todos.json")
        print(f"{Fore.GREEN}Todo item '{item}' created successfully!{Style.RESET_ALL}")

    def read(self):
        if not self.todos:
            print(f"{Fore.YELLOW}No todo items found.{Style.RESET_ALL} or loading from file...")
            self.__load_from_file("todos.json")
           
        else:
            self.__load_from_file("todos.json")
            print(f"{Fore.CYAN}Todo items:{Style.RESET_ALL}")
            for i, item in enumerate(self.todos, start=1):
                print(f"{i}. \ntitle: {item.get('title')}\ndescription:  {item.get('description')},\ncreated-at:  {item.get('time')}, \nprogress: {item.get('progress')}")

    def update(self, index, new_item):
        if index < 1 or index > len(self.todos):
            print(f"{Fore.RED}Invalid index.{Style.RESET_ALL}")
        else:
            self.todos[index - 1] = new_item
            self.__save_to_file("todos.json")
            print(f"{Fore.GREEN}Todo item at index {index} updated successfully!{Style.RESET_ALL}")

    def delete(self, index):
        if index < 1 or index > len(self.todos):
            print(f"{Fore.RED}Invalid index.{Style.RESET_ALL}")
        else:
            deleted_item = self.todos.pop(index - 1)
            self.__save_to_file("todos.json")
            print(f"{Fore.GREEN}Todo item '{deleted_item}' at index {index} deleted successfully!{Style.RESET_ALL}")
def main():
    print("This is the main function")
if __name__ == "__main__":
    main()
