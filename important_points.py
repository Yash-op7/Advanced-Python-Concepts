
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

#! 2. Type hints
def total_cost(self) -> float:  #! this return float is a type hint, its not enforced in python that is the method can still return anything but this is used to have better autocomplete and readablitiy
    return unit_price * quantity # ignore this

#! Closures - A closure is a nested function that acts as a value from the outside function
def adder(value):
    def inner_function(base):
        return base+value
    return inner_function
#! inside any function we can define multiple functions with multiple levels, this acts as a function factory

adder_5 = adder(5)      #! this adder(5) returns a function that adds 5 to any value, it is dynamically made from adder()

print(adder_5(10))

#! we can use this to create different versions of an inside function dynamically

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

#! nonlocal keyword, used to modify variables outside the inner function in function closure from inside the inner functions kind of like function hoisting in js, i think