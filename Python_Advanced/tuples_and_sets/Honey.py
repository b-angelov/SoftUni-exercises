from collections import deque

working_bees = deque(int(bee) for bee in input().split())
nectar_quantities = deque(int(nectar) for nectar in input().split())
actions = deque(input().split())
funcs = {"*":lambda a,b: a*b,"/":lambda a,b: a/b if a else 0,"+":lambda a,b: a+b,"-":lambda a,b: a-b}
honey_made = 0

while working_bees and nectar_quantities:
    nectar = nectar_quantities.pop()
    if nectar >= working_bees[0]:
        bee = working_bees.popleft()
        action = actions.popleft()
        honey_made += abs(funcs[action](bee, nectar))

print(f"Total honey made: {honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(map(str,working_bees))}")
if nectar_quantities:
    print(f"Nectar left: {', '.join(map(str,nectar_quantities))}")
