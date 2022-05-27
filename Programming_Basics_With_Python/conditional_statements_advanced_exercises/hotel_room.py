month = str(input())
nights = int(input())
price = 0
apartment = 0
studio = 0

if month == "May" or month == "October":
    apartment = 65
    studio = 50
    if 7 < nights <= 14:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.70
elif month == "June" or month == "September":
    apartment = 68.70
    studio = 75.20
    if nights > 14:
        studio *= 0.80
elif month == "July" or month == "August":
    apartment = 77
    studio = 76

if nights > 14:
    apartment *= 0.90

print(f"Apartment: {nights * apartment:.2f} lv.")
print(f"Studio: {nights * studio:.2f} lv.")