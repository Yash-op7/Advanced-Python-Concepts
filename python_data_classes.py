from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(2, 1)
print(p1)
print(p1==p2)

# output is 
# Point(x=1, y=2)
# False

#! what is a dataclass? ->  a built in decorator in python (a decorator is something that will modify that is defined below it, it could be applied on a class, a function or a method, examples of decorators are @staticmethod, @classmethod), the @dataclass decorator populates the 3 common member methods: __init__ , __repr__ and the __eq__ method these are dunder methods or magic methods that allwos us to provide some special functionality to our python classes 