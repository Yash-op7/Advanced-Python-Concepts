
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

#! what happens in `for i in y` is that i = next(y), all the for loop does is call the next() function on the iterator to get the next item in the sequence

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


x = range(1, 11)

print(x)        #  just prints the string representation of x: range(1, 11)
# we cannot do next(x) directly, because it is not a iterator, for us to get the iterator from the range object we need to use a special method called iter() or .__iter__() dunder method

# iter() and .__iter__() are identical in fucntionality


print(next(iter(x)))
print(next(iter(x)))
for i in x: print(i)

# so for i in x is same as for i in iter(x)

# Define your own iterator using legacy syntax:
class Iter:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        self.current=0
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        x = self.current
        self.current+=1
        return x
    
print("defining our own legacy iterator")

myIter = Iter(5)

# for i in myIter:
#     print(i)

print(next(myIter))
print(next(myIter))
print(next(myIter))

iter2 = myIter.__iter__()
print(next(iter2))

# Create our own iterator using a generator which is a much more elegant and nicer way to define iterators compared to legacy iterators

print("Generators")
def gen(n):
    for i in range(n):
        yield i

#! that's it!

for i in gen(5):
    print(i)

# the way generators work is that when the yield i line is hit, it pauses the exectution of the function (gen(x)) and returns the value to whatever is iterating through this generator object and
# when the yield code line is hit all the information about this function is saved in memory and the function executes from that checkpoint whenever the next() is encountered again, below is a more clearer way to visualize generators

print("testing generator2")
def gen():
    yield 1
    print("resuming after the first yield")
    yield 2
    print("resuming after the 3rd yield")
    yield 3
    print("stop iter")

x = gen()
cnt = 1
for i in x:
    print(f'current iteraton is {cnt}')
    cnt+=1
    print(i)
    print(i, 'is finished so the iter is paused at statement => yield ',i)


# when to use iterators/generators -> when you want to loop through a sequence at any point in time you only care for the current element in the loop, you dont care about the previous or the future values in the sequence so use generators or iterators to save memory

# example of a good use case: say you want to check if a particular word exists in a very huge lines of 400GB, if you do it normally you would need to load the file in the code which wont be feasible so easily as the entire file must be brought to the memory or you may need to do some chunking or whatever, so what you can do is the following:
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


# Generaotr comprehension
# one way to make a generator is using a function and a yield keyword, another is the following using normal parenthesis:
x = (i for i in range(10))
print(x)    # <generator object <genexpr> at 0x1020c0940>