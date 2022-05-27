n = input()
is_special = False

for i in range(1, int(n) + 1):
    sum = 0
    stri = str(i)
    for c in range(len(stri)):
        sum += int(stri[c])
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
