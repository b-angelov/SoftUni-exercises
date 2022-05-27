year = int(input())

while True:
    year += 1
    syear = str(year)
    for i in range(len(syear)):
        if syear.count(syear[i]) > 1:
            break
    else:
        print(year)
        break