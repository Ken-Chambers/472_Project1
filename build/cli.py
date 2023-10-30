import argparse

def createParser():
    parser = argparse.ArgumentParser(description="Task Manager with Priority Queue")
    

    return parser

def main():
    parser = createParser()
    args = parser.parse_args()

main()