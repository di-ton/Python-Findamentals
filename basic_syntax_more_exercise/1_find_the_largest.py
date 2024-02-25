number = input()
number_list = [int(x) for x in str(number)]
new_list = []
for el in range(len(number_list)):
    while len(number_list) != 0:
        new_list.append(str(max(number_list)))
        number_list.remove(max(number_list))

print("".join(new_list))

