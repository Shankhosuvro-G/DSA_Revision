def addLinkedlist(l1,l2):
    ll_lst1=[]
    ll_lst2=[]
    for i in l1:
        ll_lst1.append(i)
    for i in l2:
        ll_lst2.append(i)
    num1=int("".join(map(str,ll_lst1)))
    num2=int("".join(map(str,ll_lst2)))
    total=num1+num2
    new_total=str(total)
    new_add=list(new_total)
    llstr=""
    for i in new_add:
        llstr+=i+"-->"
    print(llstr)    

## for multiplying two linked list work with the index