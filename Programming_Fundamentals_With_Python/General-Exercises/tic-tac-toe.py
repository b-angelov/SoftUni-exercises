winner = 0
row = []
for i in range(3):
    row.append(input().split(" "))
    row[i] = list(map(int,row[i]))

    if row[i][0] == row[i][1] == row[i][2]:
        winner = row[i][0]
        break
else:
    for i in range(3):
        if row[0][i] == row[1][i] == row[2][i]:
            winner = row[0][i]
            break
        elif row[0][0] == row[1][1] == row[2][2] or row[0][2] == row[1][1] == row[2][0]:
            winner = row[1][1]
            break

if not winner:
    print("Draw!")
if winner == 1:
    print("First player won")
if winner == 2:
    print("Second player won")