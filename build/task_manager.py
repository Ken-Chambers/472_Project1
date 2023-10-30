import queue

class TaskManager:
    def __init__(self):
        self.tasks = queue.PriorityQueue()
    
    def addTask(self, prior, desc):
        self.tasks.put((prior, desc))

    def listTasks(self):
        tasks = []
        while not self.tasks.empty():
            description, priority  = self.tasks.get()
            tasks.append((description, priority ))
        return tasks
