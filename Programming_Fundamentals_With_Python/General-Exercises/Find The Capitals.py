string = str(input())
out = []

for i in range(len(string)):
    if string[i].isupper():
        out.append(i)
print(out)