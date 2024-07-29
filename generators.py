# A generator in python is simliar to list comprehension in syntax and function but it returns value only when they need to be used, it doesn't store all the values, it will give you the next value when you ask for it and generate it on the fly, we are not storign all the values by pregenerating them like in a list comprehension we are only generating them when we need to use them, see example below

# Generator comprehension
# Calculate the sum of squares of all values from 1 to a 1,000,000

sum_of_squares = sum(x**2 for x in range(1, 1000001))       # space: O(1)
# the range function is going to return values one by one, its not going to generate an entire list of them in memory, 
# and the way that the sum function works is rather than executing this `for x in range(10000000)` entire block right away and getting a list and then applying sum on that list, it asks for each value sequentially and add it to an internal vairable
# this works due to generators and iterators and how some of these in-built functions are optimized

# whereas
sum2 = sum([x**2 for x in range(1000000)]) # is space: O(n)

print(sum_of_squares, sum2)
