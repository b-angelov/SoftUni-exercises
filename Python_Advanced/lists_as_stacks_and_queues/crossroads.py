from collections import deque

inputs = (int(input()),int(input()))
cars_queue = deque()
passed = 0

command = input()
while command != "END":
    if command == "green":
        green, free = inputs
        car = car_full_name = ""
        while green and (car or cars_queue):
            green -= 1
            if not car:
                car = cars_queue.popleft()
                car_full_name = car
            car = car[1:]
            if not car: passed += 1
        while free and car:
            free -= 1
            car = car[1:]
            if not car:
                passed += 1
        if car:
            print("A crash happened!",f"{car_full_name} was hit at {car[0]}.",sep="\n")
            break
    else:
        cars_queue.append(command)

    command = input()
else:
    print("Everyone is safe.",f"{passed} total cars passed the crossroads.",sep="\n")

