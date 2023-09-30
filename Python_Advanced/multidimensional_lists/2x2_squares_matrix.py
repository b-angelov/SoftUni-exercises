i,j = list(map(int,input().split()))
matrix = [input().split() for _ in range(i)]
matrices = list(filter(lambda x: len(x[0]) == 2 and x[0][0] == x[0][1] and x[0] == x[1],([matrix[r][c:c+2],matrix[r+1][c:c+2]] for r in range(i-1) for c in range(i))))
print(len(matrices))