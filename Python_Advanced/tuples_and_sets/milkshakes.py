from collections import deque

chocolates,cups_of_milk = [deque(int(n) for n in input().split(", ")) for _ in range(2)]
milk_shakes = 0

while chocolates and cups_of_milk:
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    chocolate = chocolates.pop()
    if chocolate <= 0:
        continue
    milk = cups_of_milk.popleft()
    if milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == milk:
        milk_shakes += 1
        if milk_shakes >= 5:
            break
    else:
        cups_of_milk.append(milk)
        chocolates.append(chocolate - 5)
if milk_shakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str,chocolates))}" if chocolates else "Chocolate: empty")
print(f"Milk: {', '.join(map(str,cups_of_milk))}" if cups_of_milk else  "Milk: empty")
