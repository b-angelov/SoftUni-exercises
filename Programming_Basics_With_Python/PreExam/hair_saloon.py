days_target = int(input())  # 1/5000
hair_style = str(input())  # "haircut" "color" "closed"
total = 0

while hair_style != "closed":
    if hair_style == "haircut":
        gender = str(input())  # "mens" "ladies" "kids"
        if gender == "mens":
            price = 15
        elif gender == "ladies":
            price = 20
        elif gender == "kids":
            price = 10
    elif hair_style == "color":
        type = str(input())  # "touch up" "full color"
        if type == "touch up":
            price = 20
        elif type == "full color":
            price = 30
    total += price
    if total >= days_target:
        break
    hair_style = str(input())

if total >= days_target:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {days_target - total}lv. more.")

print(f"Earned money: {total}lv.")