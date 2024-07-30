
#! A decorator is just a function that modifies another function
#! some things to note:
# first check this example

import time

def timer(func):
    def wrapper(*args, **kwargs):           # these arguements are fixed
        start_time = time.time()
        result = func(*args, **kwargs)      # call the decorated function, and store the result
        end_time = time.time()
        print(f"finished execution in {end_time-start_time}")
        return result                       # return the result of the decorated function so that what we essentially did is that we ensure the origianlly function's job but we also performed some additionally functionality

    return wrapper                          # we must return this 

@timer
def sum_squares(n: int) -> int:
    return sum([x for x in range(n)])

# sum_squares = timer(sum_squares)

result = sum_squares(1000000)

#! So note that:
#! 1. the function with the decorators is same as sum_squares=timer(sum_squares)

