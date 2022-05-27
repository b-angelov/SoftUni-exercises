import math

days_missing = int(input())  #  1/5000
food_provided_kg = int(input())  # 0/100 000
first_deer_daily_food = float(input())  #  0.00/100.00
second_deer_daily_food = float(input())  #  0.00/100.00
third_deer_daily_food = float(input())  #  0.00/100.00

food_left = food_provided_kg - (first_deer_daily_food + second_deer_daily_food + third_deer_daily_food) * days_missing

if food_left >=0:
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    print(f"{math.ceil(abs(food_left))} more kilos of food are needed.")