airspace = [list(input()) for _ in range(int(input()))]
jet = next((rn, pn) for rn, row in enumerate(airspace) for pn, place in enumerate(row) if place == "J")
enemy_jets = sum(1 for row in range(len(airspace)) for col in range(len(airspace[row])) if airspace[row][col] == "E")
DEFAULT_ARMOR = 300
HIT_POINTS = 100
armor = 300
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while enemy_jets and armor:
    direction = input()
    jr,jc = jet
    nr,np = jr+directions[direction][0], jc+directions[direction][1]
    jet = nr,np
    sign = airspace[nr][np]
    airspace[jr][jc] = "-"
    airspace[nr][np] = "J"
    if sign == "E":
        enemy_jets -= 1
        if enemy_jets:
            armor -= HIT_POINTS
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{nr}, {np}]!")
                break
        else:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
    elif sign == "R":
        armor = DEFAULT_ARMOR

print(*(''.join(row) for row in airspace),sep="\n")
