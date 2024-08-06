from collections import deque
class stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
s=stack()
str="We will conquer Covid 19"
words=str.split()
reversed_words=[word[::-1] for word in words]
print(reversed_words)
def check_balanced(s):
    stack=[]
    open=["({["]
    close=[")}]"]
    match={"(":")","{":"}","[":"]"}
    for i in s:
        if i in open:
            stack.append(i)
            return True
        elif i in close:
            if not stack or stack.pop()!=match:
                return False
print(check_balanced("({a+b})"))            



        