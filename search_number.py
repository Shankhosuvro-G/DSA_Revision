def search_number(arr,k):
    arr.sort()
    length=len(arr)
    left=0
    right=length-1
    while left <= right:
        middle_index=(left+right)//2
        if arr[middle_index]==k:
            return middle_index
        elif arr[middle_index] < k:
            left=middle_index+1
        elif arr[middle_index] > k:
            right=middle_index-1
    return -1
print(search_number([1,2,3,4,5],5))

























    