def reverse_string(s):
    words=s.split()
    lst=[]
    for i in words:
        lst.append(i)
    lst.reverse()
    return " ".join(lst)
print(reverse_string("hello world"))