import sys
smallest = sys.maxsize
biggest = -sys.maxsize
inp = int(input())

for i in range(0,inp):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")