"""
Sample Input

10      -    number of array(data set) elements
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060 - array elements


Sample Output

43900.6    -     mean
44627.5    -    median
4978       -     mode
"""

import numpy as np
from scipy import stats

n = int(input())

# get a string input, convert it to list of strings, convert the list 
    # to an array, cast the array of strings to array of integers.
x = np.array(input().split(" ")).astype(np.int32)

print(np.mean(x))
print(np.median(x))
print(stats.mode(x)[0][0])
