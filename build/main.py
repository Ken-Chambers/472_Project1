from cli import createParser, main as cli_main
from task_manager import TaskManager
from thread_manager import ThreadManager

def main():
    parser = createParser()
    args = parser.parse_args()

    task_manager = TaskManager()
    thread_manager = ThreadManager(task_manager)

    if args.command == "add":
        task_description = args.description
        task_priority = args.priority
        task_manager.addTask(task_description, task_priority)
    elif args.command == "list":
        tasks = task_manager.listTasks()
        if tasks:
            print("Tasks: ")
            while not task_manager.tasks.empty():
                description, priority = task_manager.tasks.get()
                print(f"Description: {description}, Priority: {priority}")
        else:
            print("No tasks to print, try adding a task first")

    elif args.command == "run":
        thread_manager.runTasks()
    elif args.command == "exit":
        thread_manager.stopThreads()
    else:
        print("Invalid command. Use 'add', 'list', 'run', or 'exit'.")



main()
