def add(a, b):
    return a + b
def pow(base=1, exp=1):
    return base ** exp;

functions = [add, pow, pow, add]
arguements = [
    [(1, 2), {}],
    [(), {"base": 2, "exp":3}],
    [(), {"base": 4, "exp": 3}],
    [(3, 4), {}]
]

for func, (args, kwargs) in zip(functions, arguements):
    result = func(*args, **kwargs)
    print(result)

#! also
def function_calling_a_function(func, *args, **kwargs):
    #! the kwargs variable inside this function is a key-value dictionary, we use ** to spread the contents of that dictionary into a list of keyword arguements which are passed to func() 
    #! similarly we use * to spread args variable whihc is a tuple of positional arguements
    return func(*args, **kwargs)

def test(*args, **kwargs):
    print(args, kwargs, *args)
test(3, a=4, b=4)