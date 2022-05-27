stars = int(input())
int = 0
rev = False

while True:
    if int == stars:
        rev = True
    for i in range(0, int):
        print("*", end="")
    print()
    if rev:
        int -= 1
        if int == 0:
            break
    else:
        int += 1