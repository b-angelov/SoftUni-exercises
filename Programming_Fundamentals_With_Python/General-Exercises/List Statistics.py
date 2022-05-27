lines = int(input())
positives, negatives = [], []

for i in range(lines):
    num = int(input())
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)

print(f"{positives}\n{negatives}\nCount of positives: {len(positives)}\nSum of negatives: {sum(negatives)}")
