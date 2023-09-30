from collections import deque

cups_capacities = deque(int(capacity) for capacity in input().split())
filled_bottles = deque(int(contained) for contained in input().split())
wasted_water = 0
cup = 0

while filled_bottles and (cups_capacities or cup):
    bottle = filled_bottles.pop()
    if not cup:
        cup = cups_capacities.popleft()
    cup -= bottle
    if cup <= 0:
        wasted_water += abs(cup)
        cup = 0

if not cups_capacities:
    print(f"Bottles: {' '.join(str(filled_bottles.pop()) for _ in range(len(filled_bottles)))}" )
else:
    print(f"Cups: {' '.join(str(cups_capacities.popleft()) for _ in range(len(cups_capacities)))}")

print(f"Wasted litters of water: {wasted_water}")
