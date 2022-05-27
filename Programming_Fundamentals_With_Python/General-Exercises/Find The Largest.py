number = input()
out = ""

for i in range(9, -1, -1):
    count = str(number).count(str(i))
    for a in range(count):
        out += str(i)

print(out)
