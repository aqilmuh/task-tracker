import json
import datetime

with open("tasks.json", "r") as f:
    tasks = json.load(f)

print("Task Tracker App")

def display_tasks():
    print("\nTasks:")
    for task in tasks["tasks"]:
        print(f"""{task['id']}. {task['title']}
        Status: {task['status']}
        Deadline: {task['deadline']}
        (Due in {(datetime.datetime.strptime(task['deadline'], '%Y-%m-%d') - datetime.datetime.now()).days} days)
        """)
        

def add_task():
    title = input("Enter task title: ")
    try:
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        datetime.datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    new_task = {
        "id": len(tasks["tasks"]) + 1,
        "title": title,
        "status": "pending",
        "deadline": deadline
    }
    tasks["tasks"].append(new_task)
    print("Task added successfully!")

def update_task():
    task_id = int(input("Enter task ID to update: "))
    for task in tasks["tasks"]:
        if task["id"] == task_id:
            new_status = input("Enter new status (pending/completed): ")
            task["status"] = new_status
            print("Task updated successfully!")
            return
    print("Task not found!")

def delete_task():
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        for i, task in enumerate(tasks["tasks"]):
            if task["id"] == task_id:
                tasks["tasks"].pop(i)
                print("Task deleted successfully!")
                return

        print("Task not found!")

def main():
    while True:
        print("\nMenu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent=4)
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()