from collections import deque

petrol_pumps_number = int(input())
petrol_pumps = deque()

for pump in range(petrol_pumps_number):
    capacity,distance = map(int,input().split())
    petrol_pumps.append((capacity,distance))

index = 0
while True:
    tank = 0
    # if all((tank:=tank + a-b) >= 0 for a,b in petrol_pumps):
    for a,b in petrol_pumps:
        tank += a-b
        if tank < 0:
            break
    else:
        print(index)
        break
    petrol_pumps.append(petrol_pumps.popleft())
    index += 1
