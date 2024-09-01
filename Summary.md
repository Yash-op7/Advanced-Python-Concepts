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