budget = float(input())
season = str(input())
destination = "Europe"
vacation_type = "Hotel"
spending = 1.00

if budget <= 100:
    destination = "Bulgaria"
    if season == "winter":
        spending = 0.70
    else:
        spending = 0.30
elif budget <= 1000:
    destination = "Balkans"
    if season == "winter":
        spending = 0.80
    else:
        spending = 0.40
else:
    spending = 0.90
if season != "winter" and destination != "Europe":
    vacation_type = "Camp"

print("Somewhere in " + destination)
print(f"{vacation_type} - {budget * spending:.2f}")

