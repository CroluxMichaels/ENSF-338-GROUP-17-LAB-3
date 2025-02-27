import sys
sys.setrecursionlimit(20000)
import random
import timeit
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def generate_test_cases(size, case):
    if case == "best":
        return list(range(size))
    elif case == "worst":
        return list(range(size, 0, -1))
    else:
        return random.sample(range(size * 10), size) 

def measure_time(sort_function, arr):
    return timeit.timeit(lambda: sort_function(arr.copy()), number=1)

def analyze_performance():
    sizes = [i * 50 for i in range(1, 21)]  
    cases = ["best", "worst", "average"]
    
    results = {case: {"bubble": [], "quick": []} for case in cases}
    
    for size in sizes:
        for case in cases:
            test_data = generate_test_cases(size, case)
            
            bubble_time = measure_time(bubble_sort, test_data)
            quick_time = measure_time(quicksort, test_data)
            
            results[case]["bubble"].append(bubble_time)
            results[case]["quick"].append(quick_time)
    
    for case in cases:
        plt.figure()
        plt.plot(sizes, results[case]["bubble"], label="Bubble Sort", marker='o')
        plt.plot(sizes, results[case]["quick"], label="Quicksort", marker='s')
        plt.xlabel("Input Size")
        plt.ylabel("Time (s)")
        plt.title(f"Sorting Performance - {case.capitalize()} Case")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    analyze_performance()
