budget = int(input())
seasons = str(input())
fishermen = int(input())
discount = 1

if seasons == "Spring":
    rent = 3000
elif seasons == "Summer" or seasons == "Autumn":
    rent = 4200
elif seasons == "Winter":
    rent = 2600

if 6 >= fishermen:
    discount = 0.90
elif 6 < fishermen <= 11:
    discount = 0.85
else:
    discount = 0.75

price = rent * discount

if fishermen % 2 == 0 and seasons != "Autumn":
    price *= 0.95

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
