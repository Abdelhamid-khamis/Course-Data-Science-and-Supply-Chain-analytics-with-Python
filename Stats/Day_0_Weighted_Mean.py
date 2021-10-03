"""
Weighted Mean example:

    that's when a professor puts some weights for quizzes, attendance,
        final exam, etc..
    
    then well calculate the weighted mean of a student's score, by
        the sum of multliplied weights and scores, divided by the sum of
        all weights 


Sample Input

5                   -       n = the number of elements in array x
10 40 30 50 20      -       x = array elements
1 2 3 4 5           -       w = weighted array elements


Sample Output

32.0
"""


arr_number = int(input())
print("arr_number: ",arr_number)

arr_element = [int(i) for i in input().split(" ")] 
print("arr_element: ",arr_element)

weighted_arr_element = [int(j) for j in input().split(" ")]
print("weighted_arr_element: ",weighted_arr_element)

new_list = []
indx = 0
for indx in range(arr_number):
    new_list.append(arr_element[indx]* weighted_arr_element[indx])
print("new_list: ",new_list)
print("weighted mean: ",round(sum(new_list)/sum(weighted_arr_element),1))
