
#! 1. print() function
# print("hello", 23, sep="!") # overwrite the default behavior of print function to use ' ' as a seperator

# print("by default print function adds a \\n, to overwrite it use the end arguement", end = " $ ")
# print("Yo")

#! 2. help() function
# help(print) # prints out the documentation of a function so you don't have to look it up on the web, what it does is reads the docstrings of the function

# it also works for your own functions like so:


# def my_func(a, **kwargs):
#     """
#     a: number of cats
#     b: a dictionary pertaining to the properties of a cat

#     returns: nothign, just an example function to print some random stuff
#     """
#     print(a, kwargs['cat'])

# help(my_func)

#! 3. range() function
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(2, 10, 3)))
# print(list(range(10, -10, -2)))

#! 4. map() function: allows us to apply a function to every single item in an iterable object like a list, string, tuple, dict, set
strings = ["I", 'am', "focussed", "and", "determined", "to", "win", "🔥"]
# lengths = map(len, strings)
# print(list(lengths))

# def add_emoji(str):
#     return str + '🎇'

# print(list(map(add_emoji, strings)))

# syntax: map(function_name, iterable_object) -> returns an iterator which can be used to get the sequence

#! 5. Lambda functions! - a one line anonymous fuctino
# strings2 = map(lambda word: word + "🦈", strings)
# print(list(strings2))

# #! 6. filter() function - it will take every single item in the iterable object and pass it to a comparable function, if it returns true it will keep the item otherwise it will remove it from the resutl
# filtered_list = filter(lambda word: len(word) > 4, strings)
# print(list(filtered_list))

# #! 7. sum() - returns the sum of all the numbers from an iterable object.
# nums = [1, 2, 4.5, 3]
# print(sum(nums))
# #! `start` arguement
# print(sum(nums, start=-10))

# #! 8. sorted() - sort an iterable object in a given order
# sorted_nums = sorted(nums)
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)

# #! custom sort - `key` arguement
# people = [
#     {"name":"alice", "age":30},
#     {"name":"bob", "age":3},
#     {"name":"tom", "age":5},
#     {"name":"john", "age":19},
# ]
# # sorted_people = sorted(people)      #! gives error
# sorted_people = sorted(people, key = lambda person: person["age"], reverse=True)
# print(sorted_people)

# #! 9. enumerate() -> return a tuple of index and value for every single object
# tasks = ['study', 'rest', 'exercise', 'sleep', 'eat healthy']

# for index, value in enumerate(tasks):
#     print(f'{index+1}. {value}')

# tuples = [(1, 2), (2, 3), (3, 4)]
# print(list(enumerate(tasks)))       #! prints a list of tuples

#! 10. zip() - when you have two or more data structures with corresponding values and wanna iterate on them simultaneously
#! combine different iterable objets together
names = ['alice', 'bob', 'carl']
ages = [10, 20, 30, 99]
genders = ['female', 'male', 'male']

# # normal way
# for idx in range(min(len(names), len(ages))):
#     print(f'{names[idx]} is {ages[idx]}')

# # better way
# combined = list(zip(names, ages, genders))
# for name, age, gender in combined:
#     print(f'{name} is {age} and is a {gender}')
# # or
# combined = zip(names, ages, genders)
# for name, age, gender in combined:
#     print(f'{name} is {age} and is a {gender}')
# # or
# for name, age, gender in zip(names, ages, genders):
#     print(name, gender, age)

#! this also automatically handle when one iterable object has more objects than the other

#! 10. open() - can be used to open a file, read to it, write to it, and more

# this is how to properly use it

file = open("test.txt", 'w')    #! there are many options, but the important ones are 'w' - write, 'r' - read, 'a' = append
#! when you use 'w' it will overwrite a file if it already exists, essentially clear everything inside the file, so be careful with this
file.write("hello\ni wanna die :)")
