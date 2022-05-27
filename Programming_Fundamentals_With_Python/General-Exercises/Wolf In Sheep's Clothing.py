animal = input().split(", ")
animal.reverse()

if animal[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {animal.index('wolf')}! You are about to be eaten by a wolf!")
