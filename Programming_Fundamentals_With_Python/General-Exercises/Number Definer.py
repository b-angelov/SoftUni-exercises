num = float(input())
anum = abs(num)

if anum < 1 and anum != 0:
    print("small ", end="")
elif anum > 1000000:
    print("large ", end="")

if num == 0:
    print("zero")
elif num > 0:
    print("positive")
else:
    print("negative")

