import json
import os

FILE_NAME = "data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {"tasks": [], "study_hours": []}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

data = load_data()

def add_task():
    task = input("Enter a new task: ")
    data["tasks"].append({"task": task, "done": False})
    save_data(data)
    print("Task added!\n")

def view_tasks():
    if not data["tasks"]:
        print("No tasks yet.\n")
        return
    for i, t in enumerate(data["tasks"]):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")
    print()

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        data["tasks"][num-1]["done"] = True
        save_data(data)
        print("Task marked as completed!\n")
    except:
        print("Invalid choice.\n")

def log_hours():
    hours = float(input("Enter hours studied today: "))
    data["study_hours"].append(hours)
    save_data(data)
    print(f"Great job! Logged {hours} hours 💪\n")

def show_summary():
    total_tasks = len(data["tasks"])
    completed = sum(1 for t in data["tasks"] if t["done"])
    total_hours = sum(data["study_hours"])

    print("\n📊 Productivity Summary")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed}")
    print(f"Total Study Hours: {total_hours}\n")

while True:
    print("📘 STUDENT PRODUCTIVITY TRACKER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Log Study Hours")
    print("5. Show Summary")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        log_hours()
    elif choice == "5":
        show_summary()
    elif choice == "6":
        print("Stay productive 🚀 Goodbye!")
        break
    else:
        print("Invalid choice.\n")
