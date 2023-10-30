import threading, time

class ThreadManager:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.threads = []
        self.stop_threads_flag = threading.Event()

    def executeTask(self):
        while not self.stop_threads_flag.is_set():
            try: