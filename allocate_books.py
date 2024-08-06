def is_possible(arr, n, m, mid):
        students_required = 1
        current_sum = 0
        for i in range(n):
            if arr[i] > mid:
                return False
            if current_sum + arr[i] > mid:
                students_required += 1
                current_sum = arr[i]
                if students_required > m:
                    return False
            else:
                current_sum += arr[i]
        return True
    
def findPages(n, arr, m):
        if n < m:
            return -1
        
        low = max(arr)  
        high = sum(arr)  
        result = high
        
        while low <= high:
            middle = (low + high) // 2
            if is_possible(arr, n, m, middle):
                result = middle
                high = middle - 1
            else:
                low = middle + 1
        
        return result
print(findPages(4,[12,34,67,90],2))