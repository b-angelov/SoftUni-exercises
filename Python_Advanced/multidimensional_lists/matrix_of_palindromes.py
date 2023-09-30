rows,colls = list(map(int,input().split()))

for r in range(rows):
    for c in range(colls):
        print(f"{chr(r+97)}{chr(r+c+97)}{chr(r+97)}",end=" ")
    print()
