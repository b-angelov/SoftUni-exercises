actor = str(input())
academy_points = float(input())
members = int(input())

for i in range(0,members):
    name = str(input())
    points = float(input())

    points = len(name) * (points / 2)
    academy_points += points
    if academy_points >= 1250.5:
        break

if academy_points >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5 - academy_points:.1f} more!")
