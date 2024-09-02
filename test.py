import math
a = ["1", 2, '3', False]

def check_square(x):
    return (int(math.sqrt(x)) * int(math.sqrt(x)) == x)

print((check_square(36)))