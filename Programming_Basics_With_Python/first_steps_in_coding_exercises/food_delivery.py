chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegetarian_menu = int(input()) * 8.15
sum = chicken_menu + fish_menu + vegetarian_menu
sum += sum * 0.20
sum += 2.50

print(f"{sum:.2f}")

