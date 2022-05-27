lost_fights = int(input()) # 0 / 1000
helmet_price = float(input()) # 0 / 1000
sword_price = float(input()) # 0 / 1000
shield_price = float(input()) # 0 / 1000
armor_price = float(input()) # 0 / 1000
expenses = 0
shield_brakes = 0
for brake in range(1, lost_fights + 1):
    if brake % 2 == 0:
        expenses += helmet_price
    if brake % 3 == 0:
        expenses += sword_price
        if brake % 2 == 0:
            shield_brakes += 1
            expenses += shield_price
            if shield_brakes % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
