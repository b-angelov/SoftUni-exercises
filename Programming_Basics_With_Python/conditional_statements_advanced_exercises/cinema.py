type = str(input())
r = int(input())
c = int(input())

if type == "Premiere":
    income = r * c * 12
elif type == "Normal":
    income = r * c * 7.5
elif type == "Discount":
    income = r * c * 5

print(f"{income:.2f} leva")