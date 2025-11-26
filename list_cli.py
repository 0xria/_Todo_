from datetime import date
import json
import os


class Todo:
    def __init__(self, date, task, inprogress, completed):
        self.date = date
        self.task = task
        self.inprogress = inprogress
        self.completed = completed

class TodoList:
    def __init__(self):
        self.todos = load_todos()

    def add_todo(self, date, task):
        new_todo = Todo(date, task, False, False)
        self.todos.append(new_todo)
        store_todos(self.todos)

    def mark_inprogress(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].inprogress = True
            store_todos(self.todos)
            print(f"Task '{self.todos[index].task}' marked as In Progress.")
        else:
            print("Invalid Task Index.")
    
    def mark_completed(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].completed = True
            store_todos(self.todos)
            print(f"Task '{self.todos[index].task}' marked as Completed.")
        else:
            print("Invalid Task Index.")

    def view_todos(self):
        if not self.todos:
            print("No todos yet!")
        else:
            for i, todo in enumerate(self.todos):
                status = "Completed" if todo.completed else "In Progress" if todo.inprogress else "Not Started" 
                print(f"{i}. [{todo.date}] {todo.task} - {status}")

def store_todos(todo_list, filename="todos.json"):
    """Store todos to a JSON file"""
    todos_data = []
    for todo in todo_list:
        todos_data.append({
            "date": todo.date,
            "task": todo.task,
            "inprogress": todo.inprogress,
            "completed": todo.completed
        })
    
    with open(filename, "w") as f:
        json.dump(todos_data, f, indent=4)

def load_todos(filename="todos.json"): #load todos from json file
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "r") as f:
            todos_data = json.load(f)
            todos = []
            for todo_dict in todos_data:
                todo = Todo(
                    todo_dict["date"],
                    todo_dict["task"],
                    todo_dict["inprogress"],
                    todo_dict["completed"]
                )
                todos.append(todo)
            return todos
    except (json.JSONDecodeError, KeyError):
        return []

def main():
    todo_list = TodoList()

    while True:
        print("\nWhat's on Your Todo?")
        print("i. Add Todo")
        print("ii. Mark In Progress")
        print("iii. Mark Completed")
        print("iv. View Todos")
        print("v. Exit")
        print("vi. Export to HTML")

        command = input("What's Today's Agenda? ")
        
        if command == "i":
            date = input("Enter date (YYYY-MM-DD): ")
            task = input("Enter task: ")
            todo_list.add_todo(date, task)
            print("Task added successfully.")
        elif command == "ii":
            todo_list.view_todos()
            index = int(input("Enter task index to mark as in progress: "))
            todo_list.mark_inprogress(index)
        elif command == "iii":
            todo_list.view_todos()
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif command == "iv":
            todo_list.view_todos()
        elif command == "v":
            print("Exiting Todo List. Goodbye!")
        elif command == "vi":
            export_to_html(todo_list.todos)
            break
        else:
            print("Invalid Command. Please try again.")

    
def export_to_html(todos, filename="todo.html"):
    html = """
    <html>
    <head>
        <title>Todo List</title>
        <style>
            body {
                background: #000000;
                color: #00ffcc;
                font-family: 'Consolas', monospace;
                padding: 30px;
            }
            h1 {
                color: #00ffaa;
                font-size: 32px;
            }
            .task {
                padding: 12px;
                margin-bottom: 10px;
                border: 1px solid #00ffcc;
                border-radius: 6px;
            }
            .done {
                text-decoration: line-through;
                opacity: 0.5;
            }
            .progress {
                border-color: #ffaa00;
                color: #ffaa00;
            }
        </style>
    </head>
    <body>
        <h1>Ria’s Todo List</h1>
        <div>
    """

    for t in todos:
        if t.completed:
            cls = "task done"
        elif t.inprogress:
            cls = "task progress"
        else:
            cls = "task"

        html += f"<div class='{cls}'>[{t.date}] — {t.task}</div>"

    html += """
        </div>
    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(html)

    print(f"Exported to {filename}")


if __name__ == "__main__":
    main()
