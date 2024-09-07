def main() -> None:
    a=2
    b=3
    a, b = b, a
    # and
    a, *b = 1, 2, 3
    print(a, b)
    # Output: 1 [2, 3]



main()