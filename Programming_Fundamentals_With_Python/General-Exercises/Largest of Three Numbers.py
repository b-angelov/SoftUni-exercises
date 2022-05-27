numberOne = int(input())
numberTwo = int(input())
numberThree =int(input())

if numberOne > numberTwo and numberOne > numberThree:
    print(numberOne)
elif numberTwo > numberOne and numberTwo > numberThree:
    print(numberTwo)
else:
    print(numberThree)