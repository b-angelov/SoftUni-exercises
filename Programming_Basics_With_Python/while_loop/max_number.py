import sys

biggest = -sys.maxsize

while True:
    num = input()
    if num == "Stop":
        break
    if int(num) > biggest:
        biggest = int(num)

print(biggest)