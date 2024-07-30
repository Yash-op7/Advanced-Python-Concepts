
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