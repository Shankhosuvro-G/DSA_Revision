def swap(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]
def partition(arr,start,end):
    pivot_index=start
    pivot=arr[pivot_index]
    while start < end:
        while start < len(arr)-1 and arr[start] <= pivot:
            start+=1
        while arr[end] > pivot:
            end-=1
        if start < end:
            swap(start,end,arr)
    swap(pivot_index,end,arr)
    return end
def quick_sort(arr,start,end):
    if start < end:
        pivot_index=partition(arr,start,end)
        quick_sort(arr,start,pivot_index-1)
        quick_sort(arr,pivot_index+1,end)
if __name__=="__main__":
    elements=[11,9,29,7,2,15,28]
    quick_sort(elements,0,len(elements)-1)
    print(elements)
