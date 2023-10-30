import threading, time, queue

class ThreadManager:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.threads = []
        self.stop_threads_flag = threading.Event()

    def executeTask(self):
        while not self.stop_threads_flag.is_set():
            try:
                description = self.task_manager.tasks.get(block=False)
                print(f"Executing task: {description}")

                self.task_manager.tasks.task_done()
            except queue.Empty:
                break
    
    def runTasks(self):
        for i in range(2):
            thread = threading.Thread(target=self.executeTask)
            self.threads.append(thread)
            thread.start()

    def stopThreads(self):
        self.stop_threads_flag.set()
        for thread in self.threads:
            thread.join()