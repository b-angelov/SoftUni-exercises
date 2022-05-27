lines = int(input())
lis = []
num = []

for i in range(lines):
    num.append(int(input()))
command = input()

for i in range(len(num)):
    if command == "even":
        if num[i] % 2 == 0:
            lis.append(num[i])
    elif command == "odd":
        if num[i] % 2 != 0:
            lis.append(num[i])
    elif command == "negative":
        if num[i] < 0:
            lis.append(num[i])
    elif command == "positive":
        if num[i] >= 0:
            lis.append(num[i])

print(lis)
