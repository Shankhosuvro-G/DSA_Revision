def find_leaders(arr,n):
    lst=[]
    leaders=[]
    last_element=arr[-1]
    for i in range(n-1):
        for j in range(i+1,n-1):
            if arr[i]<arr[j]:
                lst.append(arr[i])
    #print(lst)
    for i in arr:
        if i not in lst:
            leaders.append(i)
    leaders.append(last_element)
    print(leaders)        
find_leaders([16, 19, 4, 3, 8, 3],6)                