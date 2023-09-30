from collections import deque

food_quantity = int(input())
queue = deque(int(n) for n in input().split())
print(max(queue))
order = 0
while queue:
    food_quantity -= order
    if queue[0] <= food_quantity:
        order = int(queue.popleft())
    else:
        break

if not queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str,queue))}")
