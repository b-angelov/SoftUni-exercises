int_list = input().split(", ")
int_list = list(map(int, int_list))
beggars_count = int(input())
beggars = []

while len(int_list) > 0:
    for beggar in range(beggars_count):
        if len(beggars) < beggar + 1:
            if len(int_list) > 0:
                beggars.append(int_list.pop(0))
            else:
                beggars.append(0)
        else:
            if len(int_list):
                val = int_list.pop(0)
            else:
                val = 0
            beggars[beggar] += val

print(beggars)
