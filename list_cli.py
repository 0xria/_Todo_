class Todo:
    def __init__(self, date, task, inprogress, completed):
        self.date = date
        self.task = task
        self.inprogress = inprogress
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, task):
        new_todo = Todo(task, False, False)
        self.todos.append(new_todo)

    def mark_inprogress(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].inprogress = True
    
    def mark_completed(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].completed = True
            self.todos[index].inprogress = True

    def list_todos(self):
        for i, todo in enumerate(self.todos):
            status = "Completed" if todo.completed else "In Progress" if todo.inprogress else "Not Started" 
            print(f"{i}. {todo.task} = {status}")

def main():
    todo = TodoList()

    while True:
        print("\nWhat's your Todo?")
        print("i. Add Todo")
        print("ii. Mark In Progress")
        print("iii. Mark Completed")
        print("iv. List Todos")
        print("v. Exit")
        command = input("What's Today's Agenda? ").strip
        
        if command == "add":

            task = input("Enter task: ")
            todo.add_todo(task)
        elif command == "list":
            todo.list_todos()
        elif command == "inprogress":
            index = int(input("Enter task index to mark as in progress: "))
            todo.mark_inprogress(index)
        elif command == "complete":
            index = int(input("Enter task index to mark as completed: "))
            todo.mark_completed(index)
        elif command == "exit":
            break
        else:
            print("Unknown command. Please try again.")
            
if __name__ == "__main__":
    main()




