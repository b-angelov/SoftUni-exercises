a,b = list(map(int,input().split()))
a = set(int(input()) for _ in range(a))
b = set(int(input()) for _ in range(b))
print("\n".join(str(n) for n in a&b))