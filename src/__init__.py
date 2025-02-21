def max(digits):
    if digits is None or len(digits) == 0:
        return None
    return max(digits)

assert max([1, 2, 3, 4, 5]) == 5
assert max([-1, -2, -3, -4]) == -1
assert max([100]) == 100
assert max([]) is None
assert max(None) is None
