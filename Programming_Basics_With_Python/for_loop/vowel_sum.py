n = str(input())
sum = 0

for o in range(0,len(n)):
    i = n[o]
    if i == "a":
       sum += 1
    elif i == "e":
        sum += 2
    elif i == "i":
        sum += 3
    elif i == "o":
        sum += 4
    elif i == "u":
        sum += 5

print(sum)