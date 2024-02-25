first_string = input()
second_string = input()

last_printed_string = first_string

for index in range(len(first_string)):
    left_part = second_string[:index + 1]
    right_part = first_string[index + 1:]
    new_string = left_part + right_part
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string


# string1 = input()
# string2 = input()
#
# while True:
#     for char1 in string1:
#         for char2 in string2:
#             string1[char1] = string2[char2]
#             if string1[char1] != string2[char2]:
#                 print(string1, end="")
