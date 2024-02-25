numbers = [int(x) for x in input().split()]
result = numbers[0]

for i in range(1, len(numbers)):
    result = result ^ numbers[i]

print(result)
