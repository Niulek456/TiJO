from src.math_lib import my_max, is_perfect

def test_my_max():
    assert my_max([1, 2, 3, 4, 5]) == 5
    assert my_max([-1, -5, -3]) == -1
    assert my_max([10]) == 10
    assert my_max([]) is None
    assert my_max(None) is None

def test_is_perfect():
    assert is_perfect(6) is True  # 6 = 1 + 2 + 3
    assert is_perfect(28) is True  # 28 = 1 + 2 + 4 + 7 + 14
    assert is_perfect(10) is False
    assert is_perfect(12) is False
    assert is_perfect(0) is False
    assert is_perfect(-6) is False

if __name__ == '__main__':
    test_my_max()
    test_is_perfect()
    print("All tests passed.")
