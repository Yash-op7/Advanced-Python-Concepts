# myList = ["apple", "dog", 5, True]
# myList2 = list()         # []

# item = myList[0]         # index must be less than n
# item2 = myList[-1]       # last item, -2 for second last item

# # for x in myList:
# # 	print(x)

# # if "dog" in myList:
# # 	print("yes")
	
# n = len(myList)

# myList.append("lemon")
# myList.insert(1, "banana")   # insert banana at index 1
# lastElement = myList.pop()   # .pop() returns the last item and also removes it
# myList.remove("apple")      # to remove an element by value, if its not present you will get a ValueError, so be careful
# # myList.clear()              # remove all elements
# myList.reverse()            # reverses in place

# myList = [3, 5, 1, 6, 2]
# # myList.sort()               # in place
# newList = sorted(myList)        # doesn't change the original list

# list3 = [0] * 5                # fast way to initialize lists

# myList2 = myList + list3        # easily concatenate two lists

# print(myList2)

# # slicing: an easy way to access subarray of your list

myList = [x for x in range(10)]     # myList is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slicedList = myList[1:5]            # [1, 2, 3, 4], start index 1 to stop index 5, index 5 is excluded
# slicedList = myList[:5]             # [0, 1, 2, 3, 4], start from the beginning
# slicedList = myList[1:]             # [1, 2, 3, 4, 5, 6, 7, 8, 9], start from 1 go till the end
# slicedList = myList[:]              # entire list  
# slicedList = myList[::2]            # [0, 2, 4, 6, 8], step index, every second item, start with first, basically i=0;i<n;i+=2
# slicedList = myList[::-1]           # nice way to reverse a list

# copying a list, shallow and deep

# original_list = [1, 2, 3, "banana"]
# copy_list = original_list   # shallow copy
# copy_list[2] = "bird"       # modifies the original
# print(copy_list)
# print(original_list)

# copy_list = original_list.copy()   # deep copy
# # or
# copy_list = list(original_list)     # also deep copy
# # or
# copy_list = original_list[:]        # also makes an actual copy, deep copy


# List comprehension

#! 1. Introduction
# values = [x+1 for x in range(10)]       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#! 2. Get all the even numbers from 0 to 50
# values = [x for x in range(51) if x % 2 == 0]

#! 3. String that strat with "a" and end in "y"
# values = ["any", "apple", "albany", "trolly", ""]
# values = [word for word in values if len(word) > 1 and word[0] == 'a' and word[-1] == 'y']
# or a nicer syntax
# values = [
#     string
#     for string in values
#     if len(string) > 1
#     if string[0] == 'a'
#     if string[-1] == 'y'
# ]

#! 4. Nested list comprehension: Flattening a matrix (a list of lists) ⭐️
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# this is the normal way
# values = []
# for list in matrix:
#     for x in list:
#         values.append(x)

values = [
    number for row in matrix for number in row
    # first for loop then the next for loop is inside the first and so on
]

#! 5. Categorize numbers as even or odd (print odd or even for each number in a list)
values = [x for x in range(10)]
# ! Tip❕ -> for understanding list comprehensions always look on the left and the right side of the for loops, any nested loops go from left to right, when the if else is on the left of the for loop we check what value do we wanna add depending on the if else condition inside the for loop, whereas when the for loop is on the right we are trying to filter the list
values = [
    "Even" if x % 2 == 0 else "Odd" for x in range(10)
    # ! this syntax ->     "Even" if x % 2 == 0 else "Odd" is valid in a lot of places in python, you can put it in variables
]

#! 6. Build a 3D list
# make a 5x5x5 list with values from 1 to 5

values = []
# for x in range(5):
#     list1 = []
#     for y in range(5):
#         list2 = []
#         for z in range(5):
#             list2.append(z+1)
#         list1.append(list2)
#     values.append(list1)

values = [[[num+1 for num in range(5)] for _ in range(5)] for _ in range(5)]
# look for the exterior most for loop, whatever is to its left will get added to the values[] array, and the meaning of this syntax: for _ in range(5) is that I want to do whatever is on the left of this for loop 5 times

# ! Apply a function to each value
def square(x):
    return x*x

def valid(x):
    if x>=2:
        return True
    return False

values = [1, 2, 3]
values = [square(x) for x in values]
values = [x**2 for x in values if valid(x)]

# print(values)

# Dictionary comprehension
# pairs = [("a", 1), ("b", 2)] # a list of pairs or tuples

# my_dict = {k:v for k, v in pairs}       # value unpacking, for this to work, each "pair" in pairs must have exactly 2 entities
# print(my_dict)

# Set comprehension

nums = [1, 2, 3, 1, 3, 2, 4, 2, 1, 3]

unique_nums = {x for x in nums}     # python will know that this should be a set because you don't have any keys
print(unique_nums)  
