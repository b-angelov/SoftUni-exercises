field = []
knights = {}
n = int(input())
cell_in_range = lambda r,c: 0 <= r < len(field) and 0 <= c < len(field[r]) and field[r][c]


def calc_opponents():
    possible_positions = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
    for position in knights:
        knights[position] = 0
        for pos in possible_positions:
            r,c = position
            x,y = pos
            r+=x;c+=y
            if cell_in_range(r,c) and field[r][c] == "K":
                knights[position] += 1


for r in range(n):
    inp = list(input())
    field.append(inp)
    for c,ch in enumerate(inp):
        if ch == "K":
            knights[(r, c)] = 0

removed = 0
while knights:
    calc_opponents()
    if not any(knights[knight]>0 for knight in knights):
        break
    knight = max(knights.items(), key=lambda x: x[1])[0]
    field[knight[0]][knight[1]] = "0"
    knights.pop(knight)
    removed += 1
print(removed)
