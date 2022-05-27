budget = float(input())
statists = int(input())
clothesPrice = float(input())
scene = budget * 0.10
if statists > 150:
    clothesPrice = clothesPrice - clothesPrice * 0.10

clothesTotal = clothesPrice * statists
total = clothesTotal + scene
final = abs(budget - total)

if budget < total:
    print(f"Not enough money!\nWingard needs {final:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {final:.2f} leva left.")