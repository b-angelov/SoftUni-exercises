from collections import deque

r,c = list(map(int,input().split()))
text = deque(list(input()))
current_row = deque()

for i in range(r):
    current_row.clear()
    for j in range(c):
        if i % 2 == 0:
            current_row.append(text[0])
        else:
            current_row.appendleft(text[0])
        text.rotate(-1)
    print(*current_row,sep="")

