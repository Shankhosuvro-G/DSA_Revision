def find_word(s,w):
    count=0
    words=s.split()
    for word in words:
        if word.lower()==w:
            lst=list(word)
            if lst[0].isupper() and lst[-1].isupper():
                count+=1
    return count
#print(find_word("ComputeR computer computer computer ComputeR","computer"))
def print_pattern(n):
    for i in range(1,n+1):
        for _ in range(n-i):
            print(" ",end="")
        for j in range(1,i-1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
#print_pattern(5)
def rectangle(n):
    for i in range(1,n+1):
        for j in range(1,n+2-i):
            print(j,end="")
        for _ in range((i-1)*2):
            print("*",end="")
        for j in range(n+1-i,0,-1):
            print(j,end="")
        print()
rectangle(5)




