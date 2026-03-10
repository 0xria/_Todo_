from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import date as dt

app = Flask(__name__)
TASK_FILE = "todos.json"

def load_todos():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, KeyError):
        return []

def store_todos(todos):
    with open(TASK_FILE, "w") as f:
        json.dump(todos, f, indent=4)

@app.route("/")
def index():
    todos = load_todos()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_task():
    todos = load_todos()
    task_text = request.form.get("task")
    task_date = request.form.get("date") or str(dt.today())
    todos.append({
        "date": task_date,
        "task": task_text,
        "inprogress": False,
        "completed": False
    })
    store_todos(todos)
    return redirect(url_for("index"))

@app.route("/inprogress/<int:index>")
def mark_inprogress(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["inprogress"] = True
        store_todos(todos)
    return redirect(url_for("index"))

@app.route("/complete/<int:index>")
def mark_completed(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["completed"] = True
        store_todos(todos)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete_task(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos.pop(index)
        store_todos(todos)
    return redirect(url_for("index"))

def archive_todo(todo):
    """help to append single todo to archive file"""
    archived = []
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as f:
                archived = json.load(f)
        except json.JSONDecodeError:
            archived = []

    archived.appemd(todo)
    with open(TASK_FILE, "w") as f:
        json.dump(archived, f, indent=4)

@app.route("/delete/<int:index>")
def delete_task(index):
    todos = load_todos()
    if 0 <= index < len (todos):
        task_to_archive = todos.pop(index) #get task before removing
        archive_todo(task_to_archive) #store in archive file
        store_todos(todos) #save updated list without deleted task
    return redirect(url_for("index"))

@app.route("/archive")
def view_archive():
    if not os.path.exists(TASK_FILE):
        archived_todos = []
    else:
        with open(TASK_FILE, "r") as f:
            archived_todos = json.load(f)
    return render_template("archive.html", archived_todos=archived_todos)
if __name__ == "__main__":
    app.run(debug=True)
