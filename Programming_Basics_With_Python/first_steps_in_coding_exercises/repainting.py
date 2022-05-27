nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())
paint *= 1.10
nylon += 2
nylon *= 1.50
paint *= 14.50
diluent *= 5.00
materials = nylon + paint + diluent + 0.40
workers = (materials * 0.30) * hours
res = materials + workers
print(res)