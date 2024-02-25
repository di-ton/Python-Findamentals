def solve(num, position):
    mask = 1 << position
    specific_bit = num & mask
    lsb = specific_bit >> position
    print(lsb)


solve(2145, 5)
solve(512, 0)