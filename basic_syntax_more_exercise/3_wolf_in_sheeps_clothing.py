animals_queue = input().split(", ")
animals_queue.reverse()
sheep_counter = 0
for el in animals_queue:
    if animals_queue[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif el == "sheep":
        sheep_counter += 1
    elif el == "wolf":
        print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
        break
