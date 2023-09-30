valid_point = lambda *point: 0 <= point[0] < len(matrix) and 0 <= point[1] < len(matrix[point[0]])
valid_command = lambda command: len(command) == 5 and command[0]=="swap" and all(isinstance(e,int) and e >= 0 for e in command[1:]) and valid_point(command[1],command[2]) and valid_point(command[3],command[4])
r,c = input().split()
matrix = [list(input().split()) for _ in range(int(r))]

while True:
    command = input()
    if command == "END":
        break
    command = [int(c) if c.isdigit() else c for c in command.split()]
    if valid_command(command):
        a,b,c,d = command[1:]
        matrix[a][b],matrix[c][d] = matrix[c][d],matrix[a][b]
        print(*list(' '.join(map(str,r)) for r in matrix),sep="\n")
    else:
        print("Invalid input!" )
