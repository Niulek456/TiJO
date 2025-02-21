def is_perfect(digit):
    if digit < 2:
        return False

    sum_divisors = 0

    for i in range(1, digit):
        if digit % i == 0:
            sum_divisors += i

    return sum_divisors == digit
