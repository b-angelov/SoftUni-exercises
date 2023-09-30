field = [list(map(int,input().split())) for _ in range(int(input()))]
points = [tuple(map(int,point.split(","))) for point in input().split()]

for point in points:
    r,c = point
    value = field[r][c]
    if value < 0:
        continue
    field[r][c] = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if 0 <= i < len(field) and 0 <= j < len(field[i]) and field[i][j] > 0:
                field[i][j] -= value
print(
    f"Alive cells: {sum(1 for r in field for a in r if a > 0)}",
    f"Sum: {sum(a for r in field for a in r if a > 0)}",
    sep="\n"
)
[print(*row) for row in field]