def largest_sum(arr):
    length=len(arr)
    sum=0
    lst=[]
    #max_sum=0
    for i in range(length):
        for j in range(i+1,length):
            sum=arr[i]+arr[j]
            lst.append(sum)
    return max(lst)
print(largest_sum([-2,-1,-3,-4,-1,2,1,-5,4]))
