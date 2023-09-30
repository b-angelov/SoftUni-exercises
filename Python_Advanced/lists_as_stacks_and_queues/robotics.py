from collections import deque

robots = list(r.split("-") for r in input().split(";"))
hour,minutes,seconds = list(map(int,input().split(":")))
time = hour * (60 * 60) + minutes * 60 + seconds
time_decode = lambda time: f"{(time // (60*60))%24:02d}:{time % (60 * 60) // 60:02d}:{time % (60 * 60) % 60:02d}"
products_queue = deque()
working_queue = deque([robot,time] for robot in robots)
product = input()

while product != "End":
    products_queue.append(product)
    product = input()

while products_queue and working_queue:
    time += 1
    product = products_queue.popleft()
    for robot in working_queue:
        if robot[1] <= time:
            break
    else:
        products_queue.append(product)
        continue

    robot[1] = time + int(robot[0][1])
    print(f"{robot[0][0]} - {product} [{time_decode(time)}]")



