import queue

class TaskManager:
    def __init__(self):
        self.tasks = queue.PriorityQueue()
    
    def addTask(self, desc, prior):
        self.tasks.put((-prior, desc))

    def listTasks(self):
        for priority, description in self.tasks.queue:
            print(f"Priority: {abs(priority)}, Description: {description}")
