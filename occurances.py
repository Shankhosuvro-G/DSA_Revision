def count_occurances(arr,k):
    dict={}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict[k]
print(count_occurances([1,2,2,3,4,5],2))
    