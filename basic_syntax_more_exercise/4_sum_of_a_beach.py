string = input().lower()

counter = 0


if string.find("sand") != -1:
    counter += string.count("sand")
if string.find("water") != -1:
    counter += string.count("water")
if string.find("fish") != -1:
    counter += string.count("fish")
if string.find("sun") != -1:
    counter += string.count("sun")
print(f"{counter}")


