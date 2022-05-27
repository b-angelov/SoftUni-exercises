number = int(input())

for i in range(2, 10):
    if i != number and number % i == 0:
        print(False)
        break
else:
    print(True)