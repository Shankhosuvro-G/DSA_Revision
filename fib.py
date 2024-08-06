def gen_fib(n):
    n1=0
    n2=1
    lst=[]
    lst.append(n1)
    lst.append(n2)
    for i in range(2,n+1):
        n3=n1+n2
        n1=n2
        n2=n3
        lst.append(n3)
    print(lst)    
gen_fib(10)