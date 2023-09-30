n = int(input())
elements = set()
for _ in range(n):
    elements.update(input().split())
print(*elements, sep="\n")