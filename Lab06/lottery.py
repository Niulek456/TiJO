def lottery(numbers: list[int], size: int | None) -> list[list[int]]:
    if size is None or size <= 0:
        return []

    seen = {}
    result = []

    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
        if seen[num] == size:
            result.append([n for n in numbers if n == num])

    return result
