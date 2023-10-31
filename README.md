# Advanced Process Manager with Process Synchronization

## Project Overview

This project aims to design and implement an advanced Process Manager with a focus on process synchronization. The Process Manager enables users to create, manage, and synchronize processes in a multi-threaded environment. It offers a command-line interface for process creation, management, and synchronization, utilizing system calls for process and thread control.

## Project Goals

- **Process Creation:** Implement process creation mechanisms using system calls like fork and exec.

- **Process Management:** Develop functionalities to list, terminate, and monitor running processes.

- **Thread Support:** Extend the Process Manager to support multiple threads within a process, including creation, termination, and synchronization mechanisms.

- **Inter-Process Communication (IPC):** Implement IPC mechanisms to allow processes and threads to communicate and share data using methods like message passing, shared memory, or pipes.

- **Process Synchronization:** Implement synchronization via mutexes and semaphores, and demonstrate their use in solving common synchronization problems.

- **Command-Line Interface:** Create a user-friendly interface for interacting with the Process Manager.

- **Logging and Reporting:** Implement logging and reporting features to track and display the execution of processes and threads.

## Project Structure

- **main.py:** Contains the command-line interface for interacting with the Process Manager, interact with it by opening the terminal.

- **process_manager.py:** Implements the Process Manager class, providing process and thread management functionalities.

## Usage

- Use the command-line interface in main.py to interact with the Process Manager via the terminal:
- List of commands:
```bash
python main.py create
python main.py list
python main.py terminate --pid <PID>
python main.py monitor --pid <PID>
python main.py create_thread --pid <PID>
python main.py list_threads --pid <PID>
python main.py terminate_thread --tid <TID>
