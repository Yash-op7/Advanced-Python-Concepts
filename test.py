
def is_input_valid(ops: list[str]) -> bool:
    expected_values: set[str] = {'+', 'D', 'C'}
    for value in ops:
        if value in expected_values:
            continue
        if not value.is:
            return False
    return True

def perfCalOps(ops: list[str]) -> int:
    return 10

def main() -> None:
    ops: list[str] = ['24', '+', "D", 'C', '4', '51']
    assert is_input_valid(ops), 'Invalid input'
    print(perfCalOps(ops))

if __name__ == '__main__':
    main()
