matrix = [list(map(int,input().split())) for _ in range(int(input()))]
operations = {"Add":lambda a,b: a+b,"Subtract": lambda a,b: a-b}

while True:
    command = input()
    if command == "END":
        break
    operation,r,c,b = tuple(int(c) if c.replace("-","").isdigit() else c for c in command.split())
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
        matrix[r][c] = operations[operation](matrix[r][c],b)
    else:
        print("Invalid coordinates")

set(print(*row) for row in matrix)