import queue

class TaskManager:
    def __init__(self):
        self.tasks = queue.PriorityQueue()
    
    def addTask(self, desc, prior):
        self.tasks.put((prior, desc))

    def listTasks(self):
        tasks = []
        while not self.tasks.empty():
            description, priortiy = self.tasks.get()
            tasks.append((description, priortiy))
        return tasks
