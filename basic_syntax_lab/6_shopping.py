budget = int(input())

current_price = input()
while current_price != "End":
    current_price = int(current_price)

    budget -= current_price
    if budget < 0:
        print("You went in overdraft!")
        exit()
    current_price = input()

print("You bought everything needed.")

# budget = int(input())
#
# total_price = 0
#
# while True:
#     command = input()
#     if command == "End":
#         print("You bought everything needed.")
#         break
#     price = int(command)
#
#     if total_price + price > budget:
#         print("You went in overdraft!")
#         break
#     total_price += price