
#! 1. Anonymous variables
items = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# to get only the second variable and have better readability
seconds = [x for _, x in items]
print(seconds)


#! 2. For-Else loop and While-Else loop to recognize early breaks whne a condition is met

items = [chr(ord('a')+i) for i in range(6)]

i=0
while i < len(items):
    if items[i] == 'c':
        print('found it')
        break
    i+=1
else:
    print("not found")

#! 3. Walrus operator := -> allows you to define and simulatenously use the variable in a condition

# example

def get_data():
    for i in range(10):
        yield i
    yield -1

gen = get_data()

while (data := next(gen)) != -1:
    print(data)

# another example to avoid recomputing or re-calling a function which could be computationally expensive

def f(x):       # asumme this is a very expensive function
    return x-1

results = [f(x) for x in range(10) if f(x) > 3]                            # this calls f(x) twice for each value which is stupid
results_walrus = [result for x in range(10) if (result := f(x)) > 3]       # ! this is better

print(results)

#! 4. Arguement unpacking -> use `*` to unpack items ƒrom an iterable obj

def print_nums(a, b, c, d):
    print(a, b, c, d)

lst = [1, 2,3 , 4]
print_nums(*lst)