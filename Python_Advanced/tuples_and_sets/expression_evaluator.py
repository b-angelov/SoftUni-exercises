from collections import deque

expression = [int(c) if c.replace("-","").isdigit() else c for c in input().split()]
funcs = dict(zip(list("*+-/"),[lambda a,b: a*b,lambda a,b:a+b,lambda a,b: a-b,lambda a,b: a//b]))
queue = deque()

for n in expression:
    if isinstance(n,int):
        queue.append(n)
    else:
        while len(queue) > 1:
            queue.insert(0,funcs[n](queue.popleft(),queue.popleft()))
print(queue[0])