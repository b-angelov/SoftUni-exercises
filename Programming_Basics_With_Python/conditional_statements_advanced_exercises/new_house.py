flowers = str(input())
quantity = int(input())
budget = int(input())
price = 0
discount = 1

if flowers == "Roses":
    price = 5
    if quantity > 80:
        discount = 0.90
elif flowers == "Dahlias":
    price = 3.80
    if quantity > 90:
        discount = 0.85
elif flowers == "Tulips":
    price = 2.80
    if quantity > 80:
        discount = 0.85
elif flowers == "Narcissus":
    price = 3
    if quantity < 120:
        discount = 1.15
elif flowers == "Gladiolus":
    price = 2.50
    if quantity < 80:
        discount = 1.20

price = (price * quantity) * discount

if price <= budget:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")