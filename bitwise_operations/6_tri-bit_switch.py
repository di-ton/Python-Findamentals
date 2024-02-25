def solve(number, position):
    mask = 7 << position
    specific_bit = number ^ mask
    print(specific_bit)


solve(1234, 7)
solve(44444, 4)