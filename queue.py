class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0,val)
        return self.queue

    def dequeue(self):
        if self.is_empty():
            return None
        else:
         self.queue.pop()
         return self.queue
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0



