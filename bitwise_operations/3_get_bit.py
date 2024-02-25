def solve(num, position=1):
    mask = 1 << 1
    specific_bit = num & mask
    result = specific_bit >> 1
    print(result)


solve(2)
solve(23)