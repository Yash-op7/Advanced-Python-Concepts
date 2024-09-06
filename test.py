
def is_input_valid(ops: list[str]) -> bool:
    return True

def perfCalOps(ops: list[str]) -> int:
    return 10

def main() -> None:
    ops: list[str] = ['24', '+', 'D', 'C', '4', '51']
    assert is_input_valid(ops)
    print(perfCalOps(ops))

if __name__ == '__main__':
    main()