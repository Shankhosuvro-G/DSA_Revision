from collections import deque

def gen_bin(n):
    result=[]
    queue=deque()
    queue.append("1")
    for i in range(n):
        front=queue.popleft()
        result.append(front)

        queue.append(front + "0")
        queue.append(front + "1")
    return result
print(gen_bin(10))
