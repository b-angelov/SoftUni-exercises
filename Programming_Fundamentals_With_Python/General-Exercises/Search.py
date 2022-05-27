number = int(input())
word = input()
strings = []

for i in range(number):
    strings.append(input())
print(strings)
for i in range(len(strings) -1, -1, -1):
    if word not in strings[i]:
        del strings[i]
print(strings)


