# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print("The length of  the string variable verse is {}".format(len(verse)))
print("the index of the first occurrence of the word 'and' in verse is {}".format(verse.find('and')))
print("the index of the last occurrence of the word 'you' in verse is {}".format(verse.rfind('you')))
print("the count of occurrences of the word 'you' in the verse is {}".format(verse.count('you')))


verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()

print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')




# --------------------------------------------------------------
verse_dict =  {'if': 3, 'you': 6,
 'can': 3, 'keep': 1,
  'your': 1, 'head': 1,
   'when': 2, 'all': 2,
    'about': 2, 'are': 1,
     'losing': 1, 'theirs': 1,
      'and': 3, 'blaming': 1,
       'it': 1, 'on': 1, 'trust': 1,
        'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}


# find number of unique keys in the dictionary
num_keys = len(verse_dict.keys())


# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict


# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(max(sorted_keys))

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]


"""
I/p = items = ['first string', 'second string']

o/p = html_str
<ul>
<li>first string</li>
<li>second string</li>
</ul>
"""
items = ['first string', 'second string']
html_str_list = ["<ul>"]
for item in items:
        html_str_list.append("<li> {} </li>".format(item))
html_str_list.append("</ul>")
html_str = "\n".join(html_str_list)


book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
book_title_dict = {}
for book_title_name in book_title:
        if book_title_name in book_title_dict:
                book_title_dict[book_title_name] += 1 
        else:
                book_title_dict[book_title_name] = 1

word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word,1)


## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_sum = 0
odd_count = 0

while odd_count <5:
        for num in num_list:
                if num %2 != 0:
                        print(num)
                        odd_sum += num
                        odd_count += 1


print(odd_sum)


check_prime = [26, 39, 51, 53, 57, 79, 85]

factors_list = []
for number in check_prime:
    for count in range(1,number+1):
# number is not prime if modulo is 0        
        if number % count == 0:
                print("{} is not a prime number".format(number))
        else:
                print("{} is a prime number".format(number))

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))



def chunker(iterable, size):    # (range(25), 4)
    # Implement function here
    for index in iterable:
            yield index

for chunk in chunker(range(25), 4):
    print(list(chunk))

# Generator expressions comprehension
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares