"""
Quartile
The quartiles of an ordered data set are the 3 points that split the data set into 4 equal groups. 
The 3 quartiles are defined as follows:


Q1: The first quartile is the middle number between the smallest number in a data set and its median.
Q2: The second quartile is the median (50th percentile) of the data set.
Q3: The third quartile is the middle number between a data set's median and its largest number.



Example 1
We will consider the following ordered dataset for this example:

    6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49

The median of the dataset is 40. As there are an odd number of data points, 
we do not include the median (the central value in the ordered list) in either half:

    Lower half: 6, 7, 15, 36, 39

    Upper half: 41, 42, 43, 47, 49

The median of the lower half is 15, so the value of the first quartile is 15, 
and the median of the upper half is 43, so the value of the third quartile is 43.


Sample Input

9                       the number of elements in the array.
3 7 8 5 12 14 21 13 18  space-separated integers describing the array's elements.

Sample Output

6        Q1
12       Q2
16       Q3
"""





#                       Steps for calculation the first, 2nd, 3rd and Inner Quartile


# Get the data(number of arr elements, arr)
elements_no = 8
str_data_set = "3 7 8 5 12 14 21 13"
# elements_no = int(input())
# str_data_set = input()


# convert list string items to list of integers, then, sort the list ascending
data_set =[]
for point in str_data_set.split(" "):
    data_set.append(int(point))
data_set.sort()

# check if the number of elements in the list is odd or even

# # if odd, find the middle value, and this is the median(2nd quartile)
if elements_no % 2 != 0:
    Q2 = data_set[len(data_set) - int((len(data_set) / 2)+ .5)]
    
    # # # Then, get the first half of the list, 
    first_half = data_set[ : data_set.index(Q2)]
    
    # # # Then, get the indexes of the middle values. 
    first_index = (int(len(first_half) / 2) - 1)
    second_index = (int(len(first_half) / 2))
    
    # # # find the middle value of it, this is the first quartile
    Q1 = int((first_half[first_index] + first_half[second_index]) / 2)
    
    
    # Then, get the second half of the list, and find the middle value of it, this is the third quartile
    second_half = data_set[data_set.index(Q2)+1:]
    first_index = (int(len(second_half) / 2) - 1)
    second_index = (int(len(second_half) / 2))

    Q3 = int((second_half[first_index] + second_half[second_index]) / 2)      
        
        
# if even, find the middle two values, and divide them by 2, and this is the median Q2
else:
    if (elements_no/2) % 2 != 0:            # for number of elements are 10 and after the division will be odd number

        first_index = (int(len(data_set) / 2) - 1)
        second_index = (int(len(data_set) / 2))
    
        Q2 = int((data_set[first_index] + data_set[second_index]) / 2)

        # then, get the first half of the list, and find middle value of it, this is Q1
        first_half = data_set[:int(len(data_set) / 2)]
        first_index = (int(len(first_half) / 2) - 1)
        second_index = (int(len(first_half) / 2))    
    
        Q1 = first_half[len(first_half) - int((len(first_half) / 2)+ .5)]

        # Then, get the second half of the list, and find the middle value of it, this is the third quartile Q3
        second_half = data_set[int(len(data_set) / 2):]
        first_index = (int(len(second_half) / 2) - 1)
        second_index = (int(len(second_half) / 2))
        Q3 = second_half[len(second_half) - int((len(second_half) / 2)+ .5)]

    else:
        first_index = (int(len(data_set) / 2) - 1)
        second_index = (int(len(data_set) / 2))
    
        Q2 = int((data_set[first_index] + data_set[second_index]) / 2)

        # then, get the first half of the list, and find middle value of it, this is Q1
        first_half = data_set[:int(len(data_set) / 2)]
        first_index = (int(len(first_half) / 2) - 1)
        second_index = (int(len(first_half) / 2))    
    
        Q1 = int((first_half[first_index] + first_half[second_index]) / 2)

        # Then, get the second half of the list, and find the middle value of it, this is the third quartile Q3
        second_half = data_set[int(len(data_set) / 2):]
        first_index = (int(len(second_half) / 2) - 1)
        second_index = (int(len(second_half) / 2))
        Q3 = int((second_half[first_index] + second_half[second_index]) / 2)      


   
# IQR = Q3 - Q1
IQR = Q3 - Q1

# print the values
print(Q1)
print(Q2)
print(Q3)
# Interpret IQR: The maximum difference in (test scores) for the middle 50% of the data is "IQR - 7" points.





# Using Numpy Percentile to calculate the Quartiles
import numpy as np

array = np.array(data_set)
np.percentile(array,[25, 50, 75])

print(np.percentile(array,[25][0]))        # Q1
print(np.percentile(array,[50])[0])        # Q2 - median
print(np.percentile(array,[75])[0])        # Q3


# Using pandas DataFrame to calculate the Quartiles
import pandas as pd

df = pd.DataFrame(data_set)
df.describe()

import inspect
from numpy import percentile
inspect.getfile(percentile)


