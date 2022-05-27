n = int(input())
sum1 = 0
sum2 = 0

for i in range(0, n):
    sum1 += int(input())
print(" ")
for i in range(0, n):
    sum2 += int(input())

if sum1 == sum2:
    print(f"Yes, sum = {abs(sum1)}")
else:
    print(f"No, diff = {abs(sum1 - sum2)}")