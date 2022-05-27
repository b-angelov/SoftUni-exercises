inp = int(input())
even = 0
odd = 0

for i in range(0, inp):
    num = int(input())
    if i % 2 == 0:
        even += num
    else:
        odd += num

if even == odd:
    print(f"Yes\nSum = {even}")
else:
    print(f"No\n Diff = {abs(even - odd)}")