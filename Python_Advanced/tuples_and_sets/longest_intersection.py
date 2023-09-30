intersections = []
for _ in range(int(input())):
    a,b = [list(map(int,i.split(","))) for i in input().split("-")]
    a,b = set(range(a[0],a[1]+1)),set(range(b[0],b[1]+1))
    intersections.append(a&b)
longest = sorted(max(intersections,key=len))
print(f"Longest intersection is {longest} with length {len(longest)}")
