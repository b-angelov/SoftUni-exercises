players = input().split(", ")
maze = [input().split() for _ in range(6)]
ignore = {"Tom":False,"Jerry":False}

while True:
    x,y = eval(input())
    first,second = players
    players = second, first
    if ignore[first]:
        ignore[first] = False
        continue
    if maze[x][y] == "E":
        print(f"{first} found the Exit and wins the game!" )
        break
    elif maze[x][y] == "T":
        print(f"{first} is out of the game! The winner is {second}." )
        break
    elif maze[x][y] == "W":
        print(f"{first} hits a wall and needs to rest.")
        ignore[first] = True

