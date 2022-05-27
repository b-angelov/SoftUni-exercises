lines = int(input())
liters = 0

for i in range(lines):

    income = int(input())
    if liters + income > 255:
        print("Insufficient capacity!")
        continue
    liters += income
print(liters)
