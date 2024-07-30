# Advanced-Python-Concepts

## 1. Lists

- A collection datatype
- ordered
- mutable
- allows duplicate elements
    
    ```python
    myList = ["apple", "dog", 5, True]
    myList2 = list()         # []
    
    item = myList[0]         # index must be less than n
    item2 = myList[-1].      # last item, -2 for second last item
    
    for x in myList:
    	print(x)
    
    if "dog" in myList:
    	print("yes")
    	
    n = len(myList)
    
    myList.append("lemon")
    myList.insert(1, "banana")   # insert banana at index 1
    lastElement = myList.pop()   # .pop() returns the last item and also removes it
    myList.remove("apple")      # to remove an element by value, if its not present you will get a ValueError, so be careful
    myList.clear()              # remove all elements
    myList.reverse().           # reverses in place
    
    myList.sort()
    ```
    

# refer to this git repo: https://github.com/Yash-op7/Advanced-Python-Concepts

## The topics that I learnt are:

- `Lists.py`
    - `list()`
    - `len()`
    - `append()`
    - `pop()`
    - `insert()`
    - `clear()`
    - `remove()`
    - `reverse()`
    - `sort()`
    - `sorted()`
    - `list1 = [0] * 5`
    - concatenation of two lists with the `+` operator
    - list slicing
    - copying,  deep copy → 3 ways
        - `oldList.copy()`
        - `newlist = oldList[:]`
        - `newList = list(oldList)`
    - list comprehension - 10 examples - must revise them
    - set comprehension
    - dict comprehension
- **`important_python_concepts.py`**
    - mutable v/s immutable types in python
    - positional arguements in functions, defautl arguements, `*args` and `**kwargs` and dynamic variable unpacking or reverse args and kwargs
    - meaning of `__name__ == "__main__"`
    - meaning of `GLI` or Global Interpreter Lock and cpu cores and multithreading in python
- `important_python_functions.py`
    - `print()`
    - `help()`
    - `range()`
    - `map()`
    - `lambda functions`
    - `filter()`
    - `sum()`
    - `sorted()`
    - `enumerate()`
    - `zip()`
    - `open()`
- `generators_vs_iterators.py`
    - what are iterators
    - `iter()` or `.__iter__()`  method
    - next() method
    - creating your own iterators with legacy syntax
    - creatign genreators with modern syntax
    - generator use cases
- important tips in general:
    - `items = [chr(ord('a')+i) for i in range(6)]` → items is `['a', 'b', 'c', 'd', 'e', 'f']`  (ASCII manipulation)
- `hidden_python_features.py`
    - `while-else` loop and `for-else` loop to identify whether a loop broke early or not
    - Anonymous variables for better readability
    - `:=` walrus operator
    - `defaultdict`