from collections import deque

materials = deque(int(piece) for piece in input().split())
magic_levels = deque(int(piece) for piece in input().split())
presents_made = []
presents = {150:"Doll",
250:"Wooden train",
300:"Teddy bear",
400: "Bicycle"
}

while materials and magic_levels:
    if materials[-1] == 0 or magic_levels[0] == 0:
        materials.pop() if not materials[-1] else None
        magic_levels.popleft() if not magic_levels[0] else None
        continue
    box = materials.pop()
    magic = magic_levels.popleft()
    prod = box * magic
    present = presents.get(prod, None)
    if present:
        presents_made.append(present)
        continue
    if prod < 0:
        materials.append(box+magic)
    elif prod > 0:
        materials.append(box+15)

if ("Doll" in presents_made and "Wooden train" in presents_made) or ("Teddy bear" in presents_made and "Bicycle" in presents_made):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(materials.pop()) for _ in range(len(materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(magic_levels.popleft()) for _ in range(len(magic_levels)))}")

print(*list(f"{present}: {presents_made.count(present)}" for present in sorted(set(presents_made))),sep="\n")
