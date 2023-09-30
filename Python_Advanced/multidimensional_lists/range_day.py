field = []
position = (0,0)
targets = 0
hit_targets = []
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
position_in_field = lambda r,c: 0 <= r < len(field) and 0 <= c < len(field[r])


def move(direction,steps):
    global position
    steps = int(steps)
    r,c = position
    x,y = directions[direction]
    r += x * steps; c += y * steps
    if position_in_field(r,c) and field[r][c] == ".":
        position = r,c

def shoot(direction,*args):
    global targets
    r,c = position
    x,y = directions[direction]
    while position_in_field(r,c):
        if field[r][c] == "x":
            field[r][c] = "."
            targets -= 1
            hit_targets.append([r,c])
            break
        r += x;c += y

commands = {"move":move,"shoot":shoot}

for r in range(5):
    row = input().split()
    for c,v in enumerate(row):
        if v == "A":
            position = r,c
        elif v == "x":
            targets += 1
    field.append(row)

for _ in range(int(input())):
    command = input().split()
    commands[command[0]](*command[1:])
    if not targets:
        print(f"Training completed! All {len(hit_targets)} targets hit.")
        break
else:
    print(f"Training not completed! {targets} targets left.")
print(*hit_targets,sep="\n")
