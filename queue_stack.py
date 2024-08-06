from collections import deque
class Queue:
    def __init__(self):
        self.stack=deque()
    def enqueue(self,x):
        self.stack.append(x)
    def dequeue(self):
        print(self.stack[0])
        del self.stack[0]
    def front(self):
        if self.stack:
            return self.stack[0]  
    def empty(self):
        return len(self.stack) == 0
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.front()) 
queue.dequeue()
print(queue.front()) 