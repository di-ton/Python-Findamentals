divisor = int(input())
boundary = int(input())
max_value = 0
for N in range(1, boundary + 1):
    if N % divisor == 0:
        if N > max_value:
            max_value = N
print(f"{max_value}")


# divisor = int(input())
# boundary = int(input())
#
# for N in range(boundary, divisor - 1, -1):
#     if N % divisor == 0:
#         print(f"{N}")
#         break
