import time
import random

import matplotlib.pyplot as plt



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

def measure_time(sort_function, arr):
    """Measure execution time of a sorting function"""
    start = time.time()
    sort_function(arr)
    end = time.time()
    return end - start

# Define input sizes
sizes = [100, 500, 1000, 5000, 10000, 20000]
results_insertion = []
results_binary_insertion = []

for size in sizes:
    test_data = [random.randint(0, 100000) for _ in range(size)]

    # Measure time for traditional insertion sort
    arr_copy = test_data[:]
    time_insert = measure_time(insertion_sort, arr_copy)
    results_insertion.append(time_insert)

    # Measure time for binary insertion sort
    arr_copy = test_data[:]
    time_binary_insert = measure_time(binary_insertion_sort, arr_copy)
    results_binary_insertion.append(time_binary_insert)

plt.plot(sizes, results_insertion, label="Insertion Sort", marker='o')
plt.plot(sizes, results_binary_insertion, label="Binary Insertion Sort", marker='s')

plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Comparison of Insertion Sort vs Binary Insertion Sort")
plt.legend()
plt.grid(True)
plt.show()

#Q4
# Observations: 
# - Binary Insertion Sort is technically faster than Traditional Insertion Sort for larger datasets.
# - The advantage of binary search in finding the correct position reduces comparisons but does not eliminate shifts, this still takes time.
# - Traditional Insertion Sort performs better for small datasets but works worse as input size grows due to O(n²) complexity.
# - Binary Insertion Sort reduces comparison operations but has the same O(n²) time complexity due to shifting elements.

# Conclusion:
# Binary Insertion Sort is technically more efficient than Traditional Insertion Sort for larger input sizes but does not beat the performance of 
# advanced sorting algorithms like Merge Sort or Quick Sort.