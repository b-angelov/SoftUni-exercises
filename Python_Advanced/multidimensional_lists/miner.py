field_size = int(input())
command_list = input().split()
directions = {"left":(0,-1),"right":(0,1),"up":(-1,0),"down":(1,0)}
collected_coal,coal,start,end = 0,0,None,None
field = []

for r in range(field_size):
    row = input().split()
    field.append(row)
    for c,j in enumerate(row):
        if j == "c":
            coal += 1
        elif j == "s":
            start = (r,c)

for command in command_list:
    r,c = start
    x,y = directions[command]
    r,c = r+x,c+y
    if 0 <= r < len(field) and 0 <= c < len(field[r]):
        start = (r,c)
        value = field[r][c]
        if value == "e":
            print(f"Game over! ({r}, {c})")
            break
        field[r][c] = "*"
        if value == "c":
            collected_coal += 1
        if coal == collected_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
else:
    print(f"{coal-collected_coal} pieces of coal left. ({r}, {c})")
