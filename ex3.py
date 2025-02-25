import matplotlib.pyplot as plt
import random as rand
import scipy.optimize as sp

no_swaps = []
no_comparisons = []
input_size = [10, 20, 30, 40, 50]
normalized = []

def quadratic(x, a):
    return a*(x**2 - x)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def bubble_sort_count(arr):
    n = len(arr)
    numcomp = 0
    numswap = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                numswap += 1
            numcomp += 1
    no_swaps.append(numswap)
    no_comparisons.append(numcomp)
    return arr

for a in input_size:
    arr = []
    for i in range(a):
        arr.append(rand.randrange(0, 1000))
    bubble_sort_count(arr)
print(f"Comparison List: {no_comparisons}")
print(f"Swap List: {no_swaps}")

for i in range(50):
    normalized.append(i)

plt.figure()
plt.scatter(input_size, no_comparisons)
plt.xlabel("Input Size")
plt.ylabel("Number of Comparisons")
comparisons = sp.curve_fit(quadratic, input_size, no_comparisons)
comp_y = []
for i in range(50):
    comp_y.append(quadratic(i, comparisons[0][0]))
plt.plot(normalized, comp_y)
plt.savefig("ex3.4.1.jpg")
plt.show()

plt.figure()
plt.scatter(input_size, no_swaps)
plt.xlabel("Input Size")
plt.ylabel("Number of Swaps")
swaps = sp.curve_fit(quadratic, input_size, no_swaps)
swap_y = []
for i in range(50):
    swap_y.append(quadratic(i, swaps[0][0]))
plt.plot(normalized, swap_y)
plt.savefig("ex3.4.2.jpg")
plt.show()
