def solve(num, position):
    mask = ~(1 << position)
    result = num & mask

    print(result)


solve(1313, 5)
