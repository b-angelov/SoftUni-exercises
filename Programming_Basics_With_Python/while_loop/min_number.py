import sys

smallest = sys.maxsize

while True:
    num = input()
    if num == "Stop":
        break
    if int(num) < smallest:
        smallest = int(num)

print(smallest)