tail = input()
body = input()
head = input()

lis = [tail, body, head]
lis[0], lis[2] = lis[2], lis[0]
print(lis)