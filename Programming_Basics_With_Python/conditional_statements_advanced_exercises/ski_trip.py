stay = int(input())
room_type = str(input())
estimation = str(input())
unknown = 0
nights = stay - 1

discount = 0

if room_type == "room for one person":
    room = 18.00
elif room_type == "apartment":
    room = 25.00
    if 0 < nights < 10:
        discount = 0.30
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.50

elif room_type == "president apartment":
    room = 35.00
    if 0 < nights < 10:
        discount = 0.10
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.20


price = nights * (room - room * discount)
if estimation == "negative":
    price *= 0.90
elif estimation == "positive":
    price *= 1.25


print(f"{price:.2f}")
