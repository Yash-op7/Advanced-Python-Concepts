
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

#! how to use dynamic unpacking while invoking the function

def f4(a, b, c=True, d= False):
    print(a, b, c, d)

f4(*[3, 1], **{'c':'hello', 'd': 5.932421})

#! meaning of if __name__ == "__main__" : simply tells you whether or not you're running the current python file, it puts the code that you want to run whne executing this file inside the if so tht when this file's contents are imported the code inside the if doesn't run


#! GIL - Global Interpreter Lock, this is exclusive to python and essentially what this says is that any threads that needs to be executed needs to acquire the interpreter lock what that means is that you can only execute one thread at any point of time even if you have multiple cpu cores on your computer, 
#! on your computer you have a cpu, that cpu typically has multiple cores 2,4, 8, or anything, each core can execute one operation at a time, with hyperthreading and virtualization you may be able to do a few more but thats not the scope here, in other languages you can break your code into seperate threads and run those threads indepently on different cores and get performance benefits, but in python you cannot do that, even if you break it into threads and run them on different cores due the GIL only one thread can be executed at a time and there is no change in performance.