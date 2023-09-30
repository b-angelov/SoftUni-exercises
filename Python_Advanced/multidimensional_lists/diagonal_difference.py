matrix = [[int(n) for n in input().split(" ")] for _ in range(int(input()))]
left,right = [],[]
for i in range(len(matrix)):
    left.append(matrix[i][i])
    right.append(matrix[i][len(matrix[i])-i-1])
print(abs(sum(left) - sum(right)))