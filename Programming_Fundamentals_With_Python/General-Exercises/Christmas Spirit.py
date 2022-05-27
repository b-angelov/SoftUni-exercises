quantity = int(input()) # 1 / 100
days = int(input()) # 1 / 100
spirit = 0
cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost += 2 * quantity
        spirit += 5
    if day % 3 == 0:
        cost += 5 * quantity
        cost += 3 * quantity
        spirit += 13
    if day % 5 == 0:
        cost += 15 * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
        if day % 10 == 0:
            spirit -= 20
            cost += 23
            if days == day:
                spirit -= 30


print(f"Total cost: {cost}\nTotal spirit: {spirit}")