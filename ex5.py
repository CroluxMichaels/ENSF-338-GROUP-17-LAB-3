"""Standard Insertion Sort"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def binary_search(arr, key, start, end):
    """Finds the index where key should be inserted using binary search"""
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    """Binary Insertion Sort without using bisect"""
    for i in range(1, len(arr)):
        key = arr[i]
        # Find the insertion position using binary search
        pos = binary_search(arr, key, 0, i)

        # Shift elements to make space for key
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        
        arr[pos] = key  # Insert key at the correct position

# Example usage:
arr = [9, 5, 1, 4, 3]
binary_insertion_sort(arr)
print("Sorted array:", arr)

