from collections import deque
class Stack:
    def __init__(self):
        self.queue=deque()
    def push(self,x):
        self.queue.insert(0,x)    
    def pop(self):
        return self.queue.popleft()
    def top(self):
        if self.queue:
            return self.queue[0]
    def empty(self):
        return len(self.queue) == 0
stack=Stack()                 
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())
print(stack.empty())