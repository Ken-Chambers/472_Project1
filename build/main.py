from cli import createParser, main as cli_main
from task_manager import TaskManager
from thread_manager import ThreadManager

task_manager = TaskManager()
thread_manager = ThreadManager(task_manager)

def main():
    parser = createParser()
    args = parser.parse_args()

    if args.command == "add":
        task_description = args.description
        task_priority = args.priority
        task_manager.addTask(task_description, task_priority)
        print(f"Task '{task_description}' with priority {task_priority} has been added.")

    elif args.command == "list":
        tasks = task_manager.listTasks()
        if tasks:
            print("Tasks: ")
            for description, priority in tasks:
                print(f"Description: {description}, Priority: {priority}")
        else:
            print("No tasks to print, try adding a task first")
        print("All tasks listed")

    elif args.command == "run":
        thread_manager.runTasks()
    elif args.command == "exit":
        thread_manager.stopThreads()
    else:
        print("Invalid command. Use 'add', 'list', 'run', or 'exit'.")



main()
