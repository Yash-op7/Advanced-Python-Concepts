
#! 1. Mutable v/s Immutable types

# ! Immutable or cannot change types are:
str
int
float
bool
bytes
tuple

#! Mutable types are
list
set
dict

# example
x = (1, 2)
y = x
# cannot do x[0] = 3
x = (1, 2, 3)
#  y is still (1, 2)

def func(x, y, z):
    print(x, y, z)

func(1, 2, 3)
func(x=1, z=2, y=3)
func(5, z=2, y=1)
#  start with the positional arguements then do the named or keyword args

def f(x, y, z=2):       # example of a functino with optional args
    print(x, y, z)

def f2(x,y, *args):
    print(x, y, args)
# ! *args allows us to accept any number of positional arguements inside a tuple called args in the function

f2(2, 3,4 ,5 ,6 ,6, 4)

# ! **kwargs allows us to accept any number of keyword arguements

def f3(*args, **kwargs):
    print(args, kwargs)

f3(2, 3, 5, 2, 1, 5, name='tom', age=32, color='r', is_gay='false')
