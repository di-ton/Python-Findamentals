n = int(input())

for j in range(1, n + 1):
    is_special = False
    number = str(j)
    sum_digits = 0
    for char in number:
        sum_digits += int(char)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f"{number} -> {is_special}")