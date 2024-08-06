def missing_number(arr,n):
    s=(n*(n+1))//2
    actual_sum=sum(arr)
    missing_number=s-actual_sum
    return missing_number
print(missing_number([1,2,3,4,6],6))