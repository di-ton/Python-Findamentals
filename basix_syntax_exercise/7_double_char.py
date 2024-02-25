string = input()

while string != "End":
    if string != "SoftUni":
        new_string = " "
        for char in string:
            new_string += char * 2
        print(new_string)

    string = input()


# string = input()
#
# while string != "End":
#     if string != "SoftUni":
#         for char in string:
#             print(char * 2, end='')
#         print()
#     string = input()
