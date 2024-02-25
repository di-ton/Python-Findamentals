decoration = int(input())
days_left_to_Christmas = int(input())

ornament_set_price = 2
ornament_set_spirit = 5
tree_skirt_price = 5
tree_skirt_spirit = 3
tree_garland_price = 3
tree_garland_spirit = 10
tree_lights_price = 15
tree_lights_spirit = 17

days_counter = 0
spirit_points = 0
spend_money = 0

while days_left_to_Christmas != 0:
    days_counter += 1
    days_left_to_Christmas -= 1
    if days_counter % 11 == 0:
        decoration += 2
    if days_counter % 2 == 0:
        spend_money += (decoration * ornament_set_price)
        spirit_points += ornament_set_spirit
    if days_counter % 3 == 0:
        spend_money += (decoration * tree_skirt_price + decoration * tree_garland_price)
        spirit_points += tree_skirt_spirit + tree_garland_spirit
    if days_counter % 5 == 0:
        spend_money += (decoration * tree_lights_price)
        spirit_points += tree_lights_spirit

    if days_counter % 3 == 0 and days_counter % 5 == 0:
        spirit_points += 30

    if days_counter % 10 == 0:
        spirit_points -= 20
        spend_money += (tree_skirt_price + tree_garland_price + tree_lights_price)


if days_counter % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {spend_money}")
print(f"Total spirit: {spirit_points}")

