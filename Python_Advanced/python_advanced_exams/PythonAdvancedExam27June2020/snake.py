field = [list(list(input())) for _ in range(int(input()))]
commands = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
lair = [(x,y) for x in range(len(field)) for y in range(len(field[x])) if field[x][y] == "B"]
position = [(x,y) for x in range(len(field)) for y in range(len(field[x])) if field[x][y] == "S"][0]
eaten = 0

while True:
    xi,yi = position
    com = commands[input()]
    x = position[0] + com[0]
    y = position[1] + com[1]
    if x not in range(len(field)) or y not in range(len(field[x])):
        print("Game over!")
        field[xi][yi] = "."
        break
    field[xi][yi] = "."
    if (x,y) in lair:
        field[x][y] = "."
        lair.remove((x,y))
        l1,l2 = lair[0]
        field[l1][l2] = "S"
        position = (l1,l2)
        continue
    elif field[x][y] == "*":
        eaten += 1
        field[x][y] = "S"
        position = (x,y)
        if eaten == 10:
            print("You won! You fed the snake.")
            break
    else:
        position = (x,y)
        field[x][y] = "S"

print(f"Food eaten: {eaten}")
print(*list(''.join(row) for row in field),sep="\n")

