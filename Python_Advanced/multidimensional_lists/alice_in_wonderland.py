field = [[int(c) if c.lstrip("-").isdigit() else c for c in input().split()] for _ in range(int(input()))]
alice = [(r,c) for r in range(len(field)) for c in range(len(field[r])) if field[r][c] == "A"][0]
bags_of_tea = 0
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while bags_of_tea < 10:
    x,y = directions[input()]
    r,c = alice
    field[r][c] = "*"
    r+=x;c+=y
    in_field = 0 <= r < len(field) and 0 <= c < len(field[r])
    if in_field and field[r][c] != "R":
        alice = r,c
        if isinstance(field[r][c],int):
            bags_of_tea += field[r][c]
        field[r][c] = "*"
    elif in_field:
        alice = r,c
        field[r][c] = "*"
        break
    else:
        break
else:
    print("She did it! She went to the party.")
    set(print(*row) for row in field)
    exit()
print("Alice didn't make it to the tea party.")
set(print(*row) for row in field)
