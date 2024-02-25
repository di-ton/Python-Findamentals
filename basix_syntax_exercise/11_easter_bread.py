budget = float(input())
flour_price_1kg = float(input())

eggs_price = flour_price_1kg * 0.75
milk_1l = flour_price_1kg * 1.25
milk_1_bread = milk_1l / 4

easter_bread_price = flour_price_1kg + eggs_price + milk_1_bread
easter_bread_number = 0
colored_eggs = 0

while True:
    if budget - easter_bread_price > 0:
        budget -= easter_bread_price
        easter_bread_number += 1
        colored_eggs += 3

        if easter_bread_number % 3 == 0:
            colored_eggs -= (easter_bread_number - 2)
    else:
        print(f"You made {easter_bread_number} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        exit()