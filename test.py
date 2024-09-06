# Flatten a nested list
# [[1, 2], [3, 4], [5, 6]]

from typing import Union

def flatten(nested_list: Union[int, any]) -> list[int]:
    result = []
    for val in nested_list:
        if isinstance(val, int):
            result.append(val)
        else:
            result.extend(flatten(val))
    return result

def main():
    a = [[1, 2], [[29, [], [[[[45]]]]], 3, 4], [5, 6]]
    print(flatten(a))

if __name__=='__main__':
    main()
