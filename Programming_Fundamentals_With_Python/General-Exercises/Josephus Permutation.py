nums = input().split(" ")
number = int(input())

# nums = list(map(int, nums))


out = []
position = number - 1
while len(nums) > 0:
    for _ in range(position, len(nums), number):
        out.append(str(nums.pop(position)))
        position += number - 1
    else:
        position = position - len(nums)
print(f"[{','.join(out)}]")
