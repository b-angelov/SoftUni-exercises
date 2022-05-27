#print("Vacation price:")
vacation = float(input())
#print("\nArticules count:")
#print("Jigsaw:")
jigsaw = int(input())
#print("Dollies:")
dollies = int(input())
#print("Teddy Bears:")
teddyBears = int(input())
#print("Minions:")
minions = int(input())
#print("Lorries:")
lorries = int(input())
requestCount = jigsaw + dollies + teddyBears + minions + lorries

jigsaw = 2.6 * jigsaw
dollies = 3 * dollies
teddyBears = 4.10 * teddyBears
minions = 8.20 * minions
lorries = 2 * lorries

total = jigsaw + dollies + teddyBears + minions + lorries
if requestCount >= 50:
    total = total - total * 0.25
total = total - total * 0.10


if total >= vacation:
    print(f"Yes! {total-vacation:.2f} lv left.")
else:
    print(f"Not enough money! {vacation-total:.2f} lv needed.")