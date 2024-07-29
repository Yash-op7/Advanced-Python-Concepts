
# Generators Video

#! 1. Generators vs iterator

# Iterator: An iterator is an object that allows you to loop through a sequence of data without having to store all the items in the sequence in memory
# Generator: A new syntax that allows you create iterators in a better easier syntax/way
# 
# 

# what are iterators

import sys
x = [x for x in range(1, 1000)]     # assume this is hard coded, x is actually [1, 2, 3, ..., 999]

# print(sys.getsizeof(x))                 # output is 8856
# print(sys.getsizeof(range(1, 1000)))    # output is 48

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = map(lambda i: i**2, x) # ⭐️ An example of iterator, what the map function does is it takes some data structure like a list and it maps all the values in the data structure to some function, and returns an itertaor of all these function calls on all the values 
# this map function doesn't actually store the values, it is a generator or an interator

# print(y, list(y)) # y is a map object, list(y) is the list of values that y is an iterator of

print(next(y))  # output: 1
print(next(y))  # output: 4

# for i in y:
#     print(i)         # this starts from 9

# what happens in `for i in y` is that i = next(y), all the for loop does is call the next() function on the iterator to get the next item in the sequence

# print(next(y))  #! this gives StopIteration error as we have already gone through the iterator y in the for loop

# Also print(next(y)) is same as y.__next__() the dunder(double underscore) method on the object

print("dunder method")
print(y.__next__())

# Example of for loop under the hood implementation
print("starting raw for loop on iterator y")
while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("done")
        break