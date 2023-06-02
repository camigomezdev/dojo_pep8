def is_number(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_numerical_sequence(numbers: list) -> bool:
    return all(numbers[i] > numbers[i - 1] for i in range(1, len(numbers)))
