from datetime import date


class Todo:
    def __init__(self, date, task, inprogress, completed):
        self.date = date
        self.task = task
        self.inprogress = inprogress
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, date, task):
        new_todo = Todo(date, task, False, False)
        self.todos.append(new_todo)

    def mark_inprogress(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].inprogress = True
            print(f"Task '{self.todos[index].task}' marked as In Progress.")
        else:
            print("Invalid Task Index.")
    
    def mark_completed(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].completed = True
            print(f"Task '{self.todos[index].task}' marked as Completed.")
        else:
            print("Invalid Task Index.")

    def list_todos(self):
        if not self.todos:
            print("No todos yet!")
        else:
            for i, todo in enumerate(self.todos):
                status = "Completed" if todo.completed else "In Progress" if todo.inprogress else "Not Started" 
                print(f"{i}. [{todo.date}] {todo.task} - {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nWhat's on Your Todo?")
        print("i. Add Todo")
        print("ii. Mark In Progress")
        print("iii. Mark Completed")
        print("iv. List Todos")
        print("v. Exit")

        command = input("What's Today's Agenda? ")
        
        if command == "i":
            date = input("Enter date (YYYY-MM-DD): ")
            task = input("Enter task: ")
            todo_list.add_todo(date, task)
            print("Task added successfully.")
        elif command == "ii":
            todo_list.list_todos()
            index = int(input("Enter task index to mark as in progress: "))
            todo_list.mark_inprogress(index)
        elif command == "iii":
            todo_list.list_todos()
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif command == "iv":
            todo_list.list_todos()
        elif command == "v":
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print("Invalid Command. Please try again.")
            
if __name__ == "__main__":
    main()




