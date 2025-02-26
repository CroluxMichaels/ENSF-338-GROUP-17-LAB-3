import timeit
import matplotlib.pyplot as plt
import json

# NOTE: Please give the code some time to run. On one of the group's machines it takes about 10 seconds for the plot to show up.

def binary_search(src, key, init_mid):
    low = 0
    high = len(src) - 1
    mid = init_mid
    while low <= high:
        if src[mid] == key:
            return mid
        elif src[mid] > key:
            high = mid - 1
            mid = (high + low)//2
        elif src[mid] < key:
            low = mid + 1
            mid = (high + low)//2
    return -1

file1 = open(file="ex7data.json", mode="r", encoding="UTF-8")
data = json.load(file1)

file2 = open(file="ex7tasks.json", mode="r", encoding="UTF-8")
keys = json.load(file2)

arbitrary_midpoints = range(0, 1000000, 10000) 
# Evenly spaced on intervals of 1000 elements
best_midpoints = []

for i in keys:
    times = []
    for j in arbitrary_midpoints:
        times.append(timeit.timeit(stmt= lambda: binary_search(data, i, j), number=10)/10)
    lowest_time_index = times.index(min(times))
    best_midpoints.append(arbitrary_midpoints[lowest_time_index]) # Appends the midpoint that takes the minimum amount of time
    # to find the element on average.

plt.figure()
plt.xlabel("Key")
plt.ylabel("Best Midpoint")
plt.scatter(x=keys, y=best_midpoints, s=3)
plt.savefig("ex7.3.png")
plt.show()

"""
4. Comment on the graph. Does the choice of initial midpoint appear to affect performance? Why do you think is that?

The graph shows that choosing a good starting midpoint can improve performance. The actual time improvement in these cases
seems to be of about 50% depending on how good the chosen midpoint is, but these measurements were left out because they 
were not requested. Since binary search divides the array in half each time, the closer the midpoint is to the actual 
value to be found, the better the algorithm performs. If a smaller amount of midpoints were used, we would see that 
the best midpoints don't really seem to matter; this is because choosing a bad midpoint only affects the first step of the
operation, and since log_base_2(1,000,000) is about 20, that means at most performing a 21st step. This accounts for 
the extra time, but is not a huge improvement because the algorithm still has a complexity of O(log(n)). The fact that there
are many outliers supports the idea that sometimes it doesn't matter if you mess up with calibration on the first step so
long as the steps that follow divide the array evenly.
"""