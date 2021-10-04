"""


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

6                       the number of elements in arrays
6 12 8 10 20 16         space-separated integers describing the respective elements of array x
5 4 3 2 1 5             space-separated integers describing he respective frequencies specified by f   

Sample Output

9.0        IQR

"""





#                       Steps for calculation the first, 2nd, 3rd and Inner Quartile


# Get the data(number of arr elements, arr)
elements_no = 6
str_data_set = "6 12 8 10 20 16"
str_frequency = "5 4 3 2 1 5"
# elements_no = int(input())
# str_data_set = input()
# str_frequency = input()

# Multiply each list string by its frequency
## convert the frequency list of strings to list of numbers
frequency_list_numbers =  [int(str_freq) for str_freq in str_frequency.split(" ")]

#str_data_set.split(" ")
combined_data_set = []


for i in range(elements_no):
    combined_data_set += [str_data_set.split(" ")[i]] * frequency_list_numbers[i]
# repeat the str_data number by the (frequency_list_numbers) number of iteration

# convert list string items to list of integers, then, sort the list ascending
data_set =[]
for point in combined_data_set:
    data_set.append(int(point))
data_set.sort()

# check if the number of elements in the list is odd or even

# # if odd, find the middle value, and this is the median(2nd quartile)
if len(data_set) % 2 != 0:
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
    if (len(data_set)/2) % 2 != 0:            # for number of elements are 10 and after the division will be odd number

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

# Interpret IQR: The maximum difference in (test scores) for the middle 50% of the data is "IQR - 7" points.