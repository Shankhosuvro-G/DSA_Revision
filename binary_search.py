def binary_search(arr,k):
    left_index=0
    right_index=len(arr)-1

    while left_index <= right_index:
        middle_index=(left_index + right_index)//2
        if arr[middle_index]==k:
            return middle_index
        elif arr[middle_index] < k:
            left_index=middle_index + 1
        elif arr[middle_index] > k:
            right_index=middle_index - 1
    return -1
#print(binary_search([1,2,34,4,5,6],34))

### binary search but k is an index
def kth_element(k,arr1,arr2):
    arr=arr1+arr2
    arr.sort()
    left=arr[0]
    right=arr[len(arr)-1]
    while left <= right:
        middle_index=(left+right)//2
        if middle_index == k-1:
            return arr[middle_index]
        elif middle_index < k-1:
            left=middle_index+1
        else:
            right=middle_index-1
    return -1
#print(kth_element(6,[2,3,6,7,9],[1,4,9,10]))

    
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
    