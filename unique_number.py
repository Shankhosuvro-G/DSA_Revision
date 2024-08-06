def find_unique_number(arr):
    for i in arr:
        if arr.count(i)==1:
            return i
    else:
        return "No Unique elements found"
print(find_unique_number([2,4,7,2,7]))