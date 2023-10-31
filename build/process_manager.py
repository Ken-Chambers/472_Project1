import os
import time
import signal
import logging
from multiprocessing import Process, Queue, Lock
import threading

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.threads = {}
        self.lock = Lock()
        self.log = logging.getLogger('ProcessManager')
        self.message_queues = {}

    def create_process(self):
        process = Process(target=self.process_function, args=())
        process.start()
        pid = process.pid

        self.processes[pid] = {'process': process, 'threads': []}
        self.message_queues[pid] = Queue()  # Create a message queue for IPC
        return pid

    def process_function(self):
        print("Child process is running...")

        # Check if there are other processes in the message_queues
        if self.message_queues:
            target_pid = list(self.message_queues.keys())[0]
            target_queue = self.message_queues[target_pid]

            for i in range(1, 6):
                print(f"Child process working: Step {i}")
                target_queue.put(f"Step {i} result")
                time.sleep(1)
        else:
            print("No other processes found for IPC.")

    def send_message(self, target_pid, message):
        if target_pid in self.message_queues:
            self.message_queues[target_pid].put(message)

    def receive_messages(self, pid):
        if pid in self.message_queues:
            while not self.message_queues[pid].empty():
                message = self.message_queues[pid].get()
                self.log.info(f"Received message in PID {pid}: {message}")

    def list_processes(self):
        for pid, data in self.processes.items():
            self.log.info(f"PID: {pid}")

    def terminate_process(self, pid):
        try:
            os.kill(pid, signal.CTRL_BREAK_EVENT)
            self.processes[pid]['process'].join()
            del self.processes[pid]
            self.log.info(f"Process with PID {pid} terminated.")
        except ProcessLookupError:
            self.log.error(f"Process with PID {pid} not found.")

    def create_thread(self, pid):
        thread = threading.Thread(target=self.thread_function, args=(pid,))
        thread.start()
        self.processes[pid]['threads'].append(thread)

    def list_threads(self, pid):
        threads = self.processes.get(pid, {}).get('threads', [])
        if threads:
            for thread in threads:
                self.log.info(f"Thread ID: {thread.ident}")
        else:
            self.log.info(f"No threads found for PID {pid}.")

    def terminate_thread(self, tid):
        for pid, data in self.processes.items():
            for thread in data['threads']:
                if thread.ident == tid:
                    thread.join()
                    data['threads'].remove(thread)
                    self.log.info(f"Thread with TID {tid} terminated.")
                    return
        self.log.error(f"Thread with TID {tid} not found.")

    def monitor_process(self, pid):
        self.log.info(f"Monitoring process with PID: {pid}")
        process_info = self.processes.get(pid)
        if process_info:
            self.log.info(f"Process state: Running")
            self.log.info(f"Parent PID: {os.getpid()}")
        else:
            self.log.error(f"Process with PID {pid} not found.")

    def thread_function(self, pid):
        self.log.info(f"Thread started for process with PID: {pid}")
        while True:
            # Your thread functionality here
            time.sleep(1)

def setup_logging():
    logging.basicConfig(filename='process_manager.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

if __name__ == "__main__":
    setup_logging()
    manager = ProcessManager()