import sys
sys.setrecursionlimit(20000)

def merge(arr, low, mid, high):
    left = arr[low:mid+1]           # left half of the array
    right = arr[mid+1:high+1]       # right half of the array

    # pointers to use
    i = 0
    j = 0
    k = low 

    while(i < len(left) and j < len(right)):
        # compare the elements from both arrays
        if(left[i] <= right[j]):
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    # copy any remaining elements from left array
    while(i < len(left)):
        arr[k] = left[i]
        i+=1
        k+=1

    # copy any remaining elements from right array
    while(i < len(right)):
        arr[k] = right[j]
        j+=1
        k+=1
        

def merge_sort(arr, low, high):
    if (low < high):
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


arr = [8, 42, 25, 3, 3, 2, 27, 3]

merge_sort(arr, 0, len(arr)-1)

print(arr)