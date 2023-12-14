matrix_size = int(input())
matrix = [list(input()) for _ in range(matrix_size)]
entering_the_game = 100
position = next((r,c) for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == "G")
commands = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}

for command in iter(input, "end"):
    r,c = position
    nr,nc = commands[command]
    nr,nc = nr+r,nc+c
    if not (0 <= nr < matrix_size) or not (0 <= nc < matrix_size) or entering_the_game <= 0:
        print("Game over! You lost everything!")
        break
    value = matrix[nr][nc]
    position = (nr,nc)
    matrix[r][c] = "-"
    matrix[nr][nc] = "G"
    if value == '-':
        continue
    if value == "W":
        entering_the_game += 100
    elif value == 'P':
        entering_the_game -= 200
        if entering_the_game <= 0:
            print("Game over! You lost everything!")
            break
    elif value == "J":
        entering_the_game += 100000
        print(f"You win the Jackpot!\n\
End of the game. Total amount: {entering_the_game}$")
        print(*(''.join(r) for r in matrix), sep="\n")
        break
    # matrix[nr][nc] = "-"
else:
    print(f"End of the game. Total amount: {entering_the_game}$")
    print(*(''.join(r) for r in matrix), sep="\n")
