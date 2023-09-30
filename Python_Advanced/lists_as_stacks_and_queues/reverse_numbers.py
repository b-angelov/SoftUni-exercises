digits = input().split()
print(" ".join(digits.pop() for _ in range(len(digits))))