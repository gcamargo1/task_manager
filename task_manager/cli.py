import argparse

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    parser = argparse.ArgumentParser(description="Simple Task Manager CLI")
    parser.add_argument("command", choices=["add", "list"], help="Command to execute")
    parser.add_argument("--task", help="Task to add")

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        if args.task:
            task_manager.add_task(args.task)
            print("Task added successfully.")
        else:
            print("Please provide a task to add.")
    elif args.command == "list":
        task_manager.list_tasks()

if __name__ == "__main__":
    main()
