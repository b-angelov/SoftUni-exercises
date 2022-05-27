people_count = int(input())  # 1/20
season = str(input())  #  "sprint" "summer" "autumn" "winter"

if people_count <= 5:
    if season == "spring":
        price = 50.00
    elif season == "summer":
        price = 48.50 * 0.85
    elif season == "autumn":
        price = 60.00
    elif season == "winter":
        price = 86.00 * 1.08
if people_count > 5:
    if season == "spring":
        price = 48.00
    elif season == "summer":
        price = 45.00 * 0.85
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        price = 85.00 * 1.08

print(f"{price * people_count:.2f} leva.")