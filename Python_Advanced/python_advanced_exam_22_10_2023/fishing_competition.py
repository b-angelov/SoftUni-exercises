area_size = int(input())

fishing_area = [list(int(i) if i.lstrip("-").isdigit() else i for i in list(input())) for _ in range(area_size)]
position, = ((r,c) for r in range(area_size) for c in range(area_size) if fishing_area[r][c] == "S")
moves = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}

quota = 20
collected_fish = 0
command = input()

def validate_position(current_, next_, size_):
    nxt = current_ + next_
    return nxt % size_ if nxt >= 0 else size_ - 1


while command != "collect the nets":

    row,col = position
    fishing_area[row][col] = "-"
    next_row,next_col = moves[command]
    row = validate_position(row, next_row, area_size)
    col = validate_position(col, next_col, area_size)
    position = row,col

    if isinstance(fishing_area[row][col],int):
        collected_fish += fishing_area[row][col]
        fishing_area[row][col] = "-"

    if fishing_area[row][col] == "W":
        print(f"You fell into a pipwhirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
        collected_fish = 0
        exit(0)

    fishing_area[row][col] = "S"
    command = input()


if collected_fish >= quota:
    print("Success! You managed to reach the quota!")

if collected_fish < quota:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {quota - collected_fish} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

set(print(*row, sep="") for row in fishing_area)