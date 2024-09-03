class Person:

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age


def main() -> None:
    p1 = Person('Tom', 59)
    # print(p1.__name)
    quantity = 239
    print(f'{quantity = }')

if __name__=='__main__':
    main()