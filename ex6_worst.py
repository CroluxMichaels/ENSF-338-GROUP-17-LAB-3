import time
import sys
import random
sys.setrecursionlimit(20000)
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    middle = [pivot] + [x for x in arr[1:] if x == pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def quicksort_binary_search(arr, key):
    sorted_arr = quicksort(arr)
    return binary_search(sorted_arr, key)

def measure_time(search_func, arr, key):
    start = time.perf_counter()
    search_func(arr, key)
    return time.perf_counter() - start

def run_experiments(sizes):
    linear_times, binary_times = [], []
    for size in sizes:
        total_linear_time = 0
        total_binary_time = 0
        for _ in range(100):
            arr = list(range(size))  
            key = arr[-1]  
            total_linear_time += measure_time(linear_search, arr, key)
            total_binary_time += measure_time(quicksort_binary_search, arr, key)
        linear_times.append(total_linear_time / 100)
        binary_times.append(total_binary_time / 100)
    return linear_times, binary_times

def plot_results(sizes, linear_times, binary_times, title):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, marker='o', label='Linear Search')
    plt.plot(sizes, binary_times, marker='s', label='Worst-Case Quicksort + Binary Search')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (s)')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_times, binary_times = run_experiments(sizes)
plot_results(sizes, linear_times, binary_times, 'Search Performance (Worst-Case Quicksort)')

"""
- The worst-case quicksort performance is O(n^2), significantly increasing sorting time.
- Binary search remains O(log n), but the high sorting overhead makes it slower than expected.
- Linear search, while still O(n), is now more competitive for smaller input sizes.
- The plots will show that binary search benefits only at very large input sizes.
"""
