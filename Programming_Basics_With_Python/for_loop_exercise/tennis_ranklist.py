# 1. Брой турнири в които участва
# Брой турнири, в които е участвал – цяло число в интервала [1…20]
# Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# Достигнат етап от турнира – текст – W, F или SF
# Променлива за точки от турнира със стойност W = 2000 F = 1200 SF = 720
# Отпечатват се три реда в следния формат:
# Final points: {брой точки след изиграните турнири}
# Average points: {средно колко точки печели за турнир}
# {процент спечелени турнири}%
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира
# до втората цифра след десетичния знак.

tournament_participation_count = int(input())
points_on_tournament_beginning = int(input())
total_points = won = 0

for i in range(tournament_participation_count):
    tournament_participation_state = str(input())
    points = 0
    if tournament_participation_state == "W":
        points += 2000
        won += 1
    elif tournament_participation_state == "F":
        points += 1200
    elif tournament_participation_state == "SF":
        points += 720

    total_points += points

print(f"Final points: {points_on_tournament_beginning + total_points} \n"
      f"Average points: {int(total_points / tournament_participation_count)}\n"
      f"{(won / tournament_participation_count) * 100:.2f}%")