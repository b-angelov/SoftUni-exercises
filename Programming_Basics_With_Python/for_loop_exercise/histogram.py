n = int(input())
p1 = p2 = p3 = p4 = p5 = 0

for i in range(0,n):
    num = int(input())
    if 1 <= num <= 1000:
        if num < 200:
            p1 += 1
        elif num < 400:
            p2 += 1
        elif num < 600:
            p3 += 1
        elif num < 800:
            p4 += 1
        else:
            p5 += 1

#whole = p1 + p2 + p3 + p4 + p5
piece = (1000/100) * (1000 / n) / 100
p1 = piece * p1
p2 = piece * p2
p3 = piece * p3
p4 = piece * p4
p5 = piece * p5

print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%\n")
