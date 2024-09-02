- `5 // 3` -> int(5/3)
- `x = input('Enter value: ')` -> input value by default converts inputs to string, so do int(x) or float(x)
- `type()` method

# string methods
- `.upper()`
- `.lower()`
- `.capitalize()`
- `.count()` - count how many times the specific substring occurs in the string
- `'hello'*3`
- cannot do this -> `'hello'+3` ❌

# misc.
- `ord(c)` get the ascii for character c

# List/Tuples
- `list1.extend([1, 2, 5, 3])` - loops through the input arguement and calls x.append for it
- `list1.pop(index)` - optional parameter, give the index to be removed

# looping misc.
- `range()` - a function that creates a collection of numbers based on the input
    - `range(start, stop, step)`:
    - `range(stop)`
    - `range(start,stop)`

- `slice` operator: allows you to take out a slice of a collection like a string, list, tuple and make it a new variable
    - `list1[start:stop:step]`

# sets
- Unordered unique collection of items
- extremely fast for lookup, deletion and addition
- use when you only care to keep track if something exists or doesn't exist, not for tracking frequency or order of items

## Initialization
- empty set -> `x = set()`
- otherwise -> `x = {1, 42, 2}`

## Methods
- `set1.add()`
- `set1.remove()`
- `x in set1`, extremely fast compared to `x in list1`: $$O(1)$$
- set1.union(set2), intersection, difference, symmetric difference, etc

# Dict or Hash Table or Map or key-value store

Also a fast lookup
```python
x = {
        'time': 23, 
        3:5231, 
        3.1:4.5, 
        True: 'no'
    }
x['key'] = 5
x[2] = [1, 3, 4]
```
- `'key2' in x`
- `list(x.values())` and `list(x.keys())`
```python
x = {
        'time': 23, 
        3:3, 
        3.1:4.5, 
        True: 'no'
    }
x['bird']=9.3
print(list(x.values()))
print(list(x.keys()))

# Output:
# [23, 3, 4.5, 'no', 9.3]
# ['time', 3, 3.1, True, 'bird']
```

- `del x['key']`
- `list(x.items())` -> returns a list of tuples of key, value, so
- `for key, val in x.items():`

# Comprehensions
- `x = [i for i in range(50) if i%5 == 0]`
- `x = ["yes" if i<10 else "no" for i in range(50) if i%5 == 0]`
- we can do these expansions for lists, tuples, sets, dictionaries:
    - `x = {i:i*i for i in range(10)}`
    - `x = {i**3 for i in range(5)}`
    - `x = tuple(i for i in range(5))` ❗️ Note because `x = (i for i in range(5))` returns a generator object

# Functions
```python
def func():
    print('run')
    def func2():
        print('inside')
    func2()
func()
```
- can return multiple items, which would be returned in a tuple which can be unpacked:
```python
def func():
    return 4, 5, 2, [12, 3, (3)]
x = func()[2]
# OR
w, x, y, z = func()
```
- functions are objects, which can be returned

```python
def func(x):
    def func2():
        print(x)
    return func2

x = func(3)     # x stores a function object
print(x)        # <function func.<locals>.func2 at 0x7efc0eb393a0>
x()             # calling the function
```

# ⭐️ unpack operator - `*`
It seperates all the elements from a collection into individual elements, 
```python
x = [1, 2, 3, 4]
print(*x)
# this will be equivalent to below code
print(x[0], x[1], x[2], x[3])
```
here is a great example:
```python
def func(x, y):
    print(x+y)

pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(pair[0], pair[1])  # ❌ Bad way to do this
    func(*pair)     # ✅ do this instead
    
```
⭐️ You can also use this `*` unpack operator on dicts as well, but you have to use `**`:
```python
def func(x, y):
    print(x+y)

func(**{'y': 5, 'x': 2})    # order of keys doesn't matter as long as the keys match the arguement names

a = 'x'
b = 'y'
func(**{a: 1, b: 4})
```
❗️ Note: you cannot have more or less keys in the dictionary as the entire dict is unpacked and passed to the func

# `*args` and `**kwargs`
So now that we understand `*` and `**` operators, we basically know how `*args` and `**kwargs` work

```python
def func(*args, **kwargs):
    print(args, kwargs)
    
func(1, 2, 3, 4, one='hello', two='world', three=2.9021)
# Output: (1, 2, 3, 4) {'one': 'hello', 'two': 'world', 'three': 2.9021}
```
Inside `func` you can then upack the args and kwargs into individual elements and use them