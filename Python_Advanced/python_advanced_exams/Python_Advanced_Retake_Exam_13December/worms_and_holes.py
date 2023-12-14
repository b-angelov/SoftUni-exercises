from collections import deque

worms = deque(map(int, input().split()))
holes = deque(map(int, input().split()))
worms_length = len(worms)
holes_count = len(holes)
matches = 0

while worms and holes:
    hole = holes.popleft()
    while worms and worms[-1] <= 0:
        worms.pop()
    if not worms:
        holes.appendleft(hole)
        continue
    if hole == worms[-1]:
        worm = worms.pop()
        matches += 1
    else:
        worms[-1] -= 3
        continue

print(f"Matches: {matches}" if matches else "There are no matches.")
print("Every worm found a suitable hole!" if matches == worms_length else "Worms left: none" if not worms else  f"Worms left: {', '.join(map(str,worms))}")
print("Holes left: none" if not holes else f"Holes left: {', '.join(map(str,holes))}")
