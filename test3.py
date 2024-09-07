def main() -> None:
    s = 'abcd'
    print(x := s.split(sep='b'))
    print(' '.join(x))


main()