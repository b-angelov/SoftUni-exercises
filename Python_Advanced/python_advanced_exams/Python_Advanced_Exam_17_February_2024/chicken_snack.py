from collections import deque
pocket_money = deque(map(int,input().split()))
food_prices = deque(map(int,input().split()))
food_eaten = 0

while pocket_money and food_prices:
    money = pocket_money.pop()
    price = food_prices.popleft()
    if money == price:
        food_eaten += 1
    if money > price:
        food_eaten += 1
        if pocket_money:
            pocket_money[-1] += money - price


if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten:
    print(f"Henry ate: {food_eaten} food{'s' if food_eaten > 1 else ''}.")
else:
    print("Henry remained hungry. He will try next weekend again.")
