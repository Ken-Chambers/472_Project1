import argparse

def createParser():
    parser = argparse.ArgumentParser(description="Task Manager with Priority Queue")
    subparsers = parser.add_subparsers(dest="command", help="Available commands: ")
    
    addParser = subparsers.add_parser("add", help="Add a new task")
    addParser.add_argument("description", help="Add a task description")
    addParser.add_argument("priority", type=int, help="Task priority")

    listParser = subparsers.add_parser("list", help="List all existing tasks")
    runParser = subparsers.add_parser("run", help="Run tasks")
    return parser

def main():
    parser = createParser()
    args = parser.parse_args()

main()