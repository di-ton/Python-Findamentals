orders = int(input())
total_price = 0

for _ in range(orders):
    price_pre_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_pre_capsule < 0.01 or price_pre_capsule > 100.00 or days > 31 or capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    else:
        price = capsules_per_day * days * price_pre_capsule
        print(f"The price for the coffee is: ${price:.2f}")

        total_price += price
print(f"Total: ${total_price:.2f}")
