# Flatten a nested list
# [[1, 2], [3, 4], [5, 6]]

from typing import Union

def flatten(nested_list: list[Union[int, any]]) -> list[int]:
    result = []
    for val in nested_list:
        if isinstance(val, int):
            result.append(val)
        else:
            result.extend(flatten(val))
    return result



def main():
    a = [[1, 2], [[29, [], [[[[45]]]]], 3, 4], [5, 6]]

    flatten_lambda = lambda l: sum((flatten_lambda(sub) if isinstance(sub, list) else [sub] for sub in l), [])
    l = flatten_lambda(a)
    print(l)

    k = sum((x for x in range(5)), -1)
    print(k)

if __name__=='__main__':
    main()
