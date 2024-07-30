
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
lengths = map(len, strings)
print(list(lengths))

def add_emoji(str):
    return str + '🎇'

print(list(map(add_emoji, strings)))

# syntax: map(function_name, iterable_object) -> returns an iterator which can be used to get the sequence

#! 5. Lambda functions! - a one line anonymous fuctino
strings2 = map(lambda word: word + "🦈", strings)
print(list(strings2))

