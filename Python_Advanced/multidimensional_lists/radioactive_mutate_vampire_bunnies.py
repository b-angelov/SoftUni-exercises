field = []
r, c = list(map(int, input().split()))
command_list = dict(zip(list("RLUD"), ((0, 1), (0, -1), (-1, 0), (1, 0))))
player = None
bunnies = []
cell_in_range = lambda r,c: 0 <= r < len(field) and 0 <= c < len(field[r]) and field[r][c]


def spread(*position):
    player = None
    for x, y in command_list.values():
        r,c = position
        r += x
        c += y
        if cell_in_range(r,c) and field[r][c] != "B":
            if field[r][c] == "P":
                player = (r, c)
            field[r][c] = "V"
    return player

def normalize():
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "V":
                field[r][c] = "B"


def check_bunnies():
    r = None
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "B":
                r = spread(row, col)
    normalize()
    return r


for row in range(r):
    line = list(input())
    field.append(line)
    for col, char in enumerate(line):
        if char == "B":
            bunnies.append((row, col))
        elif char == "P":
            player = (row, col)

win = False
for move in list(input()):
    r,c = player
    field[r][c] = "."
    x,y = command_list[move]
    r+=x
    c+=y
    if cell_in_range(r,c):
        overcome_by_bunny = check_bunnies()
        player = (r, c)
        if field[r][c] == "B":
            break
        if overcome_by_bunny:
            player = overcome_by_bunny
            break
    else:
        check_bunnies()
        r,c = player
        if field[r][c] == "P":
            field[r][c] = "."
        win = True
        break

set(print(*row,sep="") for row in field)
print(f"won: {player[0]} {player[1]}" if win else f"dead: {player[0]} {player[1]}")



