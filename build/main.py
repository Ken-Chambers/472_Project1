import argparse
from process_manager import ProcessManager

def main():
    parser = argparse.ArgumentParser(description="Command Line Process Manager")
    parser.add_argument("action", choices=["create", "list", "terminate", "monitor", "create_thread", "list_threads", "terminate_thread"])
    parser.add_argument("--pid", type=int, help="Process ID")
    parser.add_argument("--tid", type=int, help="Thread ID")
    parser.add_argument("--data", help="Data for IPC")

    args = parser.parse_args()

    manager = ProcessManager()

    if args.action == "create":
        process_id = manager.create_process()
        print(f"Process created with PID: {process_id}")

    elif args.action == "list":
        manager.list_processes()

    elif args.action == "terminate":
        if args.pid:
            manager.terminate_process(args.pid)
        elif args.tid:
            manager.terminate_thread(args.tid)

    elif args.action == "monitor":
        if args.pid:
            manager.monitor_process(args.pid)

    # Thread operations
    elif args.action == "create_thread":
        if args.pid:
            manager.create_thread(args.pid)
            print("Thread created.")
        else:
            print("Please provide a PID for creating a thread.")

    elif args.action == "list_threads":
        if args.pid:
            manager.list_threads(args.pid)
        else:
            print("Please provide a PID to list threads for.")

    elif args.action == "terminate_thread":
        if args.tid:
            manager.terminate_thread(args.tid)

if __name__ == "__main__":
    main()