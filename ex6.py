import random
import sys
import time
sys.setrecursionlimit(20000)
import matplotlib.pyplot as plt

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def linear_search_while(arr, key):
    i = 0
    while i < len(arr) and arr[i] != key:
        i += 1
    return i if i < len(arr) else -1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
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

def run_experiments(sizes, worst_case=False):
    linear_times, binary_times = [], []
    for size in sizes:
        total_linear_time = 0
        total_binary_time = 0
        for _ in range(100):
            if worst_case:
                arr = list(range(size))  
            else:
                arr = [random.randint(0, size) for _ in range(size)]
            key = random.choice(arr)
            
            total_linear_time += measure_time(linear_search, arr, key)
            total_binary_time += measure_time(quicksort_binary_search, arr, key)
        
        linear_times.append(total_linear_time / 100)
        binary_times.append(total_binary_time / 100)
    
    return linear_times, binary_times

def plot_results(sizes, linear_times, binary_times, title):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, linear_times, marker='o', label='Linear Search')
    plt.plot(sizes, binary_times, marker='s', label='Quicksort + Binary Search')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (s)')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_times, binary_times = run_experiments(sizes)
plot_results(sizes, linear_times, binary_times, 'Search Performance on Random Inputs')

linear_times_wc, binary_times_wc = run_experiments(sizes, worst_case=True)
plot_results(sizes, linear_times_wc, binary_times_wc, 'Search Performance (Worst-Case Quicksort)')

# For small inputs: Linear Search is much faster because it does not require sorting.
# For large inputs: Linear Search still outperforms because Quicksort sorting time dominates.
# Quicksort + Binary Search is not practical unless the array is sorted beforehand, as the sorting step significantly increases runtime.