import argparse

def createParser():
    parser = argparse.ArgumentParser(description="Task Manager with Priority Queue")
    parser.add_argument("add", help="Add a new task")
    parser.add_argument("edit", help="Edit an existing task")
    parser.add_argument("list", help="List current task")
    parser.add_argument("run", help="Run a new task")


    return parser

def main():
    parser = createParser()
    args = parser.parse_args()

main()