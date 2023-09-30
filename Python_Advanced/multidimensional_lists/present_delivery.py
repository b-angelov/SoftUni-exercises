number_of_presents = int(input())
neighborhood = [input().split() for _ in range(int(input()))]
count_children = sum(1 for r in neighborhood for v in r if v in "V")
happy_children = 0
santa = [(r,c) for r in range(len(neighborhood)) for c in range(len(neighborhood[r])) if neighborhood[r][c]=="S"][0]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
position_in_neighborhood = lambda r,c,field=neighborhood: 0 <= r < len(field) and 0 <= c < len(field[r])
command = input()

while command != "Christmas morning" and number_of_presents:
    r,c = santa
    broken = False
    x,y = directions[command]
    neighborhood[r][c] = "-"
    r+=x;c+=y
    if position_in_neighborhood(r,c):
        santa = r,c
        if neighborhood[r][c] == "V":
            happy_children += 1
            number_of_presents -= 1
            neighborhood[r][c] = "S"
            if number_of_presents  == 0:
                if happy_children != count_children:
                    print("Santa ran out of presents!")
                break
        elif neighborhood[r][c] == "C":
            for a,b in directions.values():
                a+=r;b+=c
                if neighborhood[a][b] != "-":
                    if neighborhood[a][b] == "V":
                        happy_children += 1
                    number_of_presents -= 1
                    neighborhood[a][b] = "-"
                    if number_of_presents == 0:
                        if happy_children != count_children:
                            print("Santa ran out of presents!")
                        broken = True
                        break
        neighborhood[r][c] = "S"
    if broken:
        break
    command = input()
set(print(*row) for row in neighborhood)
if happy_children == count_children:
    print(f"Good job, Santa! {happy_children} happy nice kid/s.")
else:
    print(f"No presents for {count_children-happy_children} nice kid/s.")