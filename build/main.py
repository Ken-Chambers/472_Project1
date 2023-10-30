from cli import createParser, main as cli_main
from task_manager import TaskManager
from thread_manager import ThreadManager

def main():
    parser = createParser()
    args = parser.parse_args()

    if args.command == "add":
        task_description = args.description
        task_priority = args.priority
        task_manager.addTask(task_description, task_priority)
    elif args.command == "list":
        task_manager.listTasks()
    elif args.command == "run":
        thread_manager.runTasks()
    elif args.command == "exit":
        thread_manager.stopThreads()
    else:
        print("Invalid command. Use 'add', 'list', 'run', or 'exit'.")



task_manager = TaskManager()
thread_manager = ThreadManager(task_manager)
main()
