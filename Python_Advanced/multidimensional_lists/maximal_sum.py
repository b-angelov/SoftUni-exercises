matrix = [list(map(int,input().split())) for _ in range(int(input().split()[0]))]
points = {(r,c):0 for r in range(0,len(matrix)-2) for c in range(0,len(matrix[r])-2)}

for square in points.keys():
    points[square] = sum(matrix[r][c] for r in range(square[0],square[0]+3) for c in range(square[1],square[1]+3))

square,ssum = max(points.items(),key=lambda x: x[1])
print(f"Sum = {ssum}",
      *list(' '.join(str(matrix[r][c]) for c in range(square[1],square[1]+3)) for r in range(square[0],square[0]+3)),
      sep="\n")