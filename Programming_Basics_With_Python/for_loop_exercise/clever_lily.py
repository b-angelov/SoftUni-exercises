age = int(input())
wm_price = float(input())
toy_price = int(input())
toys = 0
money = 0
increasing = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        increasing += 10
        money += increasing - 1
    else:
        toys += 1

toys *=  toy_price
money += toys

if money >= wm_price:
    print(f"Yes! {money - wm_price:.2f}")
else:
    print(f"No! {wm_price - money:.2f}")