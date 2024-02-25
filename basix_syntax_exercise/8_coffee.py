command = input()
coffee_number = 0

while command != "END":
    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        coffee_number += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        coffee_number += 2

    command = input()

if coffee_number > 5:
    print("You need extra sleep")
else:
    print(f"{coffee_number}")

