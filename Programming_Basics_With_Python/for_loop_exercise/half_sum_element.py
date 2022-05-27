n = int(input())
sum = 0
biggest = 0

for i in range(1,n+1):
    num = int(input())
    sum += num
    if num > biggest:
        biggest = num

if sum - biggest == biggest:
    print(f"Yes\nSum = {sum - biggest}")
else:
    print(f"No\nDiff = {abs((sum - biggest) - biggest)}")