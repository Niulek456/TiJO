def add (first, second):
    return first + second

if __name__ == "__main__":
    assert add(1, 2) == 3

def test_addition():
    first_number = 1
    second_number = 2

    result = add(first_number, second_number)

    assert result == 3
