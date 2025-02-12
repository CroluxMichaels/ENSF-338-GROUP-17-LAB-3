import matplotlib.pyplot as plt
import numpy as np
import random as rand
import scipy.optimize as sp

"""
Questions 1 and 4 go into a pdf. Working on here for now.
1. Derive the formulas for (i) number of comparisons, and (ii) average-case number of swaps for bubble sort [0.4 pts]

(i) The number of comparisons is the same for arrays of the same size because the current element is always compared to the next,
in order to check if they should be swapped in the case that the current is bigger than the next. However, because each time we
decrease the number of elements we look at (the max element bubbles to the end of the array), we decrease the number of comparisons
each time. There are n-1 comparisons in the first pass, so:
no_comparisons = n-1 + n-2 + n-3 + (...) + 1 or summation from i = 1 to i = n-1 of i. Thanks to Gauss we know that the closed form 
of this expression is (n-1)(n)/2 or (n^2 - n)/2 which corresponds to a complexity of O(n^2)

(ii) The average-case number of swaps is similar to the number of comparisons. This is because in the average case, on each iteration
there will be half as many swaps as there will be comparisons. Therefore it approximates to 1/2 * (n^2 - n)/2 or just (n^2 - n)/4

2. Implement a version of bubble sort that counts the number of comparisons and swaps for each execution [0.2 pts]

3. Run your code on a number of inputs of increasing size (note: inputs must be appropriate for average-case complexity analysis) [0.2 pts]

4. Separately plot the results of #comparisons and #swaps by input size, together with appropriate interpolating functions.
Discuss your results: do they match your complexity analysis? [0.2 pts]
They do match complexity analysis. Because the number of comparisons is the same in all three cases, we can test our expression, and it is
in fact accurate to say (n^2 - n)/2, as for examples such as n = 10 we have that (n^2 - n)/2 evaluates to 45, exactly what the number of
comparisons is. This is the same for other input size. For number of swaps, the values vary, but on average 

"""
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
    comp_y.append(quadratic(comparisons[0][0], comparisons[1][0]))
print(comp_y)
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
    swap_y.append(quadratic(swaps[0][0], swaps[1][0]))
print(swap_y)
plt.plot(normalized, swap_y)
plt.savefig("ex3.4.2.jpg")
plt.show()
