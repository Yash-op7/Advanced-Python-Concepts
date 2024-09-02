# Lists
- Can have multiple types
- `aa = ["apple", 'd', 3, 9.3]`

## Initialization:
1. a = [1, 2]
2. a = list()
3. a = list([2, 3])
4. `[0]*5`
5. `concat_list = list1 + list2`

## Accessing elements ⭐️
- 0 ... n-1 and -n ... -1

## Functions
- `len(list1)`
- `a.append(value)`
- `a.insert(index, value)`: inserts value at index and pushes everything to the right
- `a.pop()`: returns the end value and removes it
- `a.remove(value)`: if the value is not present you will get a `ValueError`
- `a.clear()`
- `a.reverse()`: reverses in place
- `a.sort()`: modifies orginal
- `b = sorted(a)`: doesn't modify original

## Slicing ⭐️
An easy way to access subarrays of a list

- `slicedList = a[1:5]`: start at index 1 and stop at index 5, index 5 is excluded
- `slicedList = a[:3]`: from 0 ... 2
- `slicedList = a[1:3]`: from 1 to 2
- `slicedList = a[:]`: duplicate the entire list
- `slicedList = myList[::2]`: step index, every second item, start with first, basically `i=0;i<n;i+=2`
- `slicedList = myList[::-1]`: nice way to reverse a list

## Copying a list
### 1. Shallow copy
- `a = [1, 2, 3]`
- `b = a`

Modifying one also modifies the other since both are same memory allocations

### 2. Deep Copy ⭐️
3 ways:
1. `b = a.copy()`
2. `b = list(a)`
3.  `b = a[:]`

## List Comprehension
I will start off with some basic list comprehensions, but they'll quickly get less trivial.

- `values = [x+1 for x in range(10)] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- `values = [x for x in range(51) if x % 2 == 0]`
- 
```python
values = [word for word in values if len(word) > 1 and word[0] == 'a' and word[-1] == 'y']
# OR, a nicer way is ⭐️
values = [
    string
    for string in values
    if len(string) > 1
    if string[0] == 'a'
    if string[-1] == 'y'
]

```

### Nested List Comprehension ⭐️
`Flattening a list of lists, or a 2D matrix`
Nested list comprehension: Flattening a matrix (a list of lists) ⭐️

Example: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

```python
values = [
    number for row in matrix for number in row
]
# first for loop then the next for loop is inside the first and so on
```
- Other list comprehensions:

```python
values = [
    "Even" if x % 2 == 0 
    else "Odd" 
    for x in range(10)
]
```
- This syntax ->
`"Even" if x % 2 == 0 else "Odd"` is valid in a lot of places in python, you can also put it in variables, this is basically a ternary operator but more verbose

- ⭐️ For understanding any list comprehension always look on the left and the right side of the expression, any nested loops go from left to right, when the if else is on the left of the for loop we check what value do we wanna insert depending on the if else condition, whereas when the for loop is on the right we are trying to filter from the list

- For example to create a 5x5x5 list: ⭐️ 
```python
values = [[[num+1 for num in range(5)] for _ in range(5)] for _ in range(5)]
```
⭐️ Look for the exterior most for loop, whatever is to its left will get added to the values[] array, and the meaning of this syntax: for _ in range(5) is that I want to do whatever is on the left of this for loop 5 times (because I don't care about the value of the iterator variable at each iteration)

- Funtions in comprehensions:\
`values = [x**2 for x in values if valid(x)]`

# Dictionary comprehension
If we have `pairs = [("a", 1), ("b", 2)]`: a list of pairs or tuples

-> `my_dict = {k:v for k, v in pairs}`: value unpacking, for this to work, each "pair" in pairs must have exactly 2 entities

# Set comprehension

Let `nums = [1, 2, 3, 1, 3, 2, 4, 2, 1, 3]`

`unique_nums = {x for x in nums}`: python will know that this should be a set because you don't have any keys

# Data Types in brief
- `int`: Integer type, for whole numbers.
- `float`: Floating-point type, for decimal numbers.
- `list`: Ordered, mutable collection of items.
- `tuple`: Ordered, immutable collection of items.
- `range`: Immutable sequence of numbers, commonly used in for-loops.
- `str`: String type
- `dict`: Dictionary type, for key-value pairs.
- `set`: Unordered collection of unique items.
- `frozenset`: Immutable set, eg: `my_frozenset = frozenset([1, 2, 3, 4])`\
⭐️ This immutability makes frozenset hashable, meaning it can be used as a key in a dictionary or an element in another set.

- `bool`: Boolean type, for True or False values.
- `bytes`: Immutable sequence of bytes. eg: `my_bytes = b"hello"`
- `bytearray`: Mutable sequence of bytes, eg: `my_bytearray = bytearray([65, 66, 67])`
- `memoryview`: Memory view object for binary data. eg: `my_memoryview = memoryview(b"hello")`

## Type Castings:
```python
# To int:
x = int(3.14)  # x will be 3

# To float:
y = float(10)  # y will be 10.0

# To str:
s = str(100)  # s will be '100'

# To list:
l = list((1, 2, 3))  # Converts a tuple to a list

# To tuple:
t = tuple([1, 2, 3])  # Converts a list to a tuple

# To set:
s = set([1, 2, 2, 3])  # Converts a list to a set, removes duplicates

# To dict:
d = dict([(1, 'a'), (2, 'b')])  # Converts a list of tuples to a dictionary
```



# Generators and Iterators
**Iterator**: An iterator is an object that allows you to loop through a sequence of data whithout actually having to store all the items in the sequence in memory
**Generator**: A new syntax that allows you to create iterators in a better and easier way

Consider:
`x = [x for x in range(1, 1e6)]`