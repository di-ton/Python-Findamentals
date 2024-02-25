number = int(input())

for _ in range(number):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88 and code != 88 and code != 86:
        print("GREAT!")
    else:
        print("Bye.")

# n = int(input())
#
# for _ in range(n):
#     number = int(input())
#
#     if number == 88:
#         print("Hello")
#     elif number == 86:
#         print("How are you?")
#     elif number < 88:
#         print("GREAT!")
#     else:
#         print("Bye.")