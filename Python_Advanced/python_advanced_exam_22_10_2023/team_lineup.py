def team_lineup(*players):
    countries = {}

    for player, country in players:
        countries.setdefault(country,[])
        countries[country].append(player)
    countries = sorted(countries.items(), key=lambda x: (-len(x[1]),x[0]))

    res = []

    for country,players in countries:
        res.append(f"{country}:")
        res.append('\n'.join(f'  -{player}' for player in players))

    return '\n'.join(res)



print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
print()
print(team_lineup(
    ("Lionel Messi", "Argentina"),
    ("Neymar", "Brazil"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Harry Kane", "England"),
    ("Kylian Mbappe", "France"),
    ("Raheem Sterling", "England")))
print()
print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany"),
    ("Bruno Fernandes", "Portugal"),
    ("Bernardo Silva", "Portugal"),
    ("Harry Maguire", "England")))
