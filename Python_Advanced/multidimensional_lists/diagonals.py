matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
left,right = [],[]
for i in range(len(matrix)):
    left.append(matrix[i][i])
    right.append(matrix[i][len(matrix[i])-i-1])
print(f"Primary diagonal: {', '.join(map(str,left))}. Sum: {sum(left)}",
f"Secondary diagonal: {', '.join(map(str,right))}. Sum: {sum(right)}",
sep = "\n"
)