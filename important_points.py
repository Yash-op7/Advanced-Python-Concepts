
#! 1. __repr__ and __eq__ methods
#! inside python ooops you can override certain functions with a predefined name for a predefined functionality
# for example

class Point:
    x:int
    y:int

    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'
    
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y
    
p1 = Point(1, 2)
p2 = Point(3, 3)
print(p1)
print(p1 == p2)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! 2. Type hints
def total_cost(self) -> float:  #! this return float is a type hint, its not enforced in python that is the method can still return anything but this is used to have better autocomplete and readablitiy
    return unit_price * quantity # ignore this

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! Closures - A closure is a nested function that acts as a value from the outside function
def adder(value):
    def inner_function(base):
        return base+value
    return inner_function
#! inside any function we can define multiple functions with multiple levels, this acts as a function factory

adder_5 = adder(5)      #! this adder(5) returns a function that adds 5 to any value, it is dynamically made from adder()

print(adder_5(10))

#! we can use this to create different versions of an inside function dynamically

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! Decorators: a function that modifies another function
# example of a custom decorator function

def custom_decorator(func):
    def modified_func(*args, **kwargs):
        print("function is being called with", args, kwargs)
        result = func(*args, **kwargs)
        return result
    return modified_func

@custom_decorator
def func(list1, mod=2):
    return [x for x in list1 if x%mod == 0]

print(func([2, 3, 4, 5, 19, 28, 45], mod=9)) #! this is equivalent to func = custom_decorator(func)
#! so the decorator is just the shorthand syntax for passing a func to another func
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#! nonlocal keyword, used to modify variables outside the inner function in function closure from inside the inner functions kind of like function hoisting in js, i think
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#! Function annotations -> better readability and documentation doesn't actually change teh code behavior though like typescript
# simple example
def greet(name: str) -> str:
    return f'Hello, {name}'

# more advanced types examples
from typing import List, Tuple, Optional

def process_data(data: List[int]) -> Tuple[int, List[int]]:
    return (min(data), list(max(data)))

def find_max(data: Optional[List[int]] = None) -> Optional[int]:
    if data:
        return max(data)
    return None

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ! Object Multiplication
x = "hello"*5
x = [1, 2] * 5                  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
x = [(1, 2)] * 5                # [(1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
x = (1, 2) * 5                  # (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
# print(x)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ! Ternary
flag = False
x = 1 if flag else 0
# x = 2 > 3 ? 1 : 0 is NOT valid syntax
print(x)
age, smokes = 22, False
health = "Bad" if age > 60 or smokes else ("good" if age < 30 else "okay")
print("Your health is", health)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! Zip
names = ['tim', 'bob']
ages = ['12', '23']
print(list(zip(names, ages)))   # [('tim', '12'), ('bob', '23')]

for name, age in zip(names, ages):
    print(name, age)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! Sort by key

lst =[[5, 1], [3, 4]]
lst.sort(key = lambda x: x[0]+x[1], reverse=True)
print(lst)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! itertools, very cool!

import itertools

lst = [1, 2, 3, 4, 5]
prefixes = itertools.accumulate(lst)
print(list(prefixes))                   # [1, 3, 6, 10, 15] 

lst2 = ['A', 'B']
print(list(itertools.chain(lst, lst2)))
print(lst+lst2)                         # both are same

names = ['Tim', 'Bob', 'John', 'Hamilcar', 'Rose']
attendence = [1, 0, 1, 0, 1]
present_students = itertools.compress(names, attendence)        #! only gives you value that correspond to a true condition in another list
print(list(present_students))           # ['Tim', 'John', 'Rose']

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! .get() function to fetch a key from a dict and return a default value in case of KeyError
dict1 = {'name': 'yash', 'willpower': 0.6}
print(
    dict1.get('has_a_job', False)                   # change it ffs
)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! Negative indexing -> range of indexes in python lists is -n to n-1
nums = [x+1 for x in range(5)]
last_element = nums[-1]
first_element = nums[-1 * len(nums)]
all_except_last = nums[:-1]
reversed_nums = nums[::-1]
# print(nums, last_element, first_element, all_except_last, reversed_nums, sep='\n')

#! Inline swaps - no third temporary variable needed

x = 10
y = 20
print("before swap", x, y)
x, y = y, x
print("after swap", x, y)

# also

x, y = 23, 41
x, y = [3, 1]
x, y = (3, 1)
print(x, y)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#! PEP8 - Python Style Guide for better readability

#  see pep8.py

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# pip3 freeze > requirements.txt     