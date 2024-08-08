def is_balanced(s):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack is None or stack.pop()!=matching_brackets[char]:
                return False
    return True
#print(is_balanced("({a+b})") )  
def remove_one(num):
    stack=list(num)
    lst=[]
    length=len(stack)
    for i in range(0,length-1):
        if stack[i]=="1"and stack[i+1]=="0":
            lst.append(stack[i+1])
    if lst==[]:
        return num
    else:
        return lst
#print(remove_one("1110"))
def operation(num,user_input):
    if user_input=="AND":
        a=int(num[0])
        for i in num[1:]:
            a&=int(i)
        return a 
    if user_input=="OR":
        a=int(num[0])
        for i in num[1:]:
            a|=int(i)
        return a
    if user_input=="XOR":
        a=int(num[0])
        for i in num[1:]:
            a^=int(i)
        return a
print(operation("1101000111","OR"))



