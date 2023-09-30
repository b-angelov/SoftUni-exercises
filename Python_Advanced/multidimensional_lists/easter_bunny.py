n = int(input())
field = [[int(i) if i.lstrip("-").isdigit() else i for i in input().split()] for _ in range(n)]
bunny = [(r, c) for r in range(len(field)) for c in range(len(field[r])) if field[r][c] == "B"][0]
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
max_direction = [float("-inf"),None]
for direction in directions.items():
    r,c = bunny
    x,y = direction[1]
    r+=x;c+=y
    row = []
    while 0 <= r < len(field) and 0 <= c < len(field[r]) and field[r][c] != "X":
        row.append([r,c])
        r += x
        c += y
    row_value = sum(field[r][c] for r,c in row)
    if row_value >= max_direction[0]:
        max_direction[1] = (direction[0],row)
        max_direction[0] = row_value
print(max_direction[1][0],*max_direction[1][1],max_direction[0],sep="\n")
