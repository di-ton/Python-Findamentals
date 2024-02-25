n = int(input())

for _ in range(n):
    string = input()
    is_pure_string = True
    for i in string:
        if i in (",",".","_"):
            is_pure_string = False

    if not is_pure_string:
        print(f"{string} is not pure!")

    if is_pure_string:
        print(f"{string} is pure.")

