def binary_search(arr,k):
    left_index=0
    right_index=len(arr)-1

    while left_index < right_index:
        middle_index=(left_index + right_index)//2
        if arr[middle_index]==k:
            return middle_index
        elif arr[middle_index] < k:
            left_index=middle_index + 1
        elif arr[middle_index] > k:
            right_index=middle_index - 1
    return -1
#print(binary_search([1,2,34,4,5,6],34))


### all occurences
def all_occurences(arr,k):
    lst=[]
    left_index=0
    right_index=len(arr)-1
    while left_index <= right_index:
        middle_index=(left_index + right_index)//2
        if arr[middle_index] == k:
            lst.append(middle_index)
            i=middle_index-1
            while i >= 0 and arr[i]==k:
                lst.append(i)
                i-=1
            i=middle_index+1
            while i < len(arr) and arr[i]==k:
                lst.append(i)
                i+=1
            break
        elif arr[middle_index] < k:
            left_index=middle_index + 1
        elif arr[middle_index] > k:
            right_index=middle_index - 1
    return lst
#print(all_occurences([1,2,3,4,5,5,5,6,7,8],5))

##using dictionary
from collections import defaultdict
def all_occurences_dict(arr,k):
    dict=defaultdict(list)
    length=len(arr)
    for i in range(length):
        if arr[i] == k:
            dict[arr[i]].append(i)
    return dict[k]        
print(all_occurences_dict([1,2,3,4,5,5,5,6,7,8],5))
    