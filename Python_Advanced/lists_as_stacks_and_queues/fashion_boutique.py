# not completed

clothes_box,rack_capacity = list(map(int,input().split())),int(input())
racks = 1
current_rack = rack_capacity
while clothes_box:
    box = clothes_box.pop()
    if current_rack - box > 0:
        current_rack -= box
    elif current_rack - box <= 0:
        if clothes_box:
            racks += 1
        current_rack = rack_capacity - box
print(racks)