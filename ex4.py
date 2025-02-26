import timeit
import matplotlib.pyplot as plt
import scipy.optimize as sp

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quadratic(x, a):
    return a*(x**2)

arraylengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sortingtimes = []
for i in arraylengths:
    array = []
    for j in range(i, 0, -1):
        array.append(j)
    sortingtimes.append(timeit.timeit(stmt=lambda: quicksort(array, 0, len(array) - 1), number=1))

normalized = []
normalized_y = []
curvefit = sp.curve_fit(quadratic, arraylengths, sortingtimes)

for i in range(100):
    normalized.append(i)
    normalized_y.append(quadratic(i, curvefit[0][0]))
plt.figure()
plt.xlabel("Array Size")
plt.title("Sorting time (s) vs Array Size")
plt.scatter(arraylengths, sortingtimes)
plt.plot(normalized, normalized_y)
plt.savefig("ex4.4.png")
plt.show()


