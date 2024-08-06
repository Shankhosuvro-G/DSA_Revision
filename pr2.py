def find_diff(arr):
    max_diff=0
    min=arr[0]
    for i in range(1,len(arr)-1):
        current_diff=arr[i]-min
        if current_diff>max_diff:
            max_diff=current_diff
        if arr[i]<min:
            min=arr[i]
    print(max_diff)            
find_diff([ 7, 9, 5, 6, 3, 2 ])    
