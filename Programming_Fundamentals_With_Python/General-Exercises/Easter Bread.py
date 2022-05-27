budget = float(input())
flour_price_per_kg = float(input())
eggs_pack_price = flour_price_per_kg * 0.75
milk_price_per_liter = flour_price_per_kg * 1.25
price_per_loaf = flour_price_per_kg + eggs_pack_price + (milk_price_per_liter / 4)
colored_eggs = 0
counter = 0

while budget > price_per_loaf:
    counter += 1
    colored_eggs += 3
    budget -= price_per_loaf
    if counter % 3 == 0:
        colored_eggs -= counter - 2


print(f"You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

