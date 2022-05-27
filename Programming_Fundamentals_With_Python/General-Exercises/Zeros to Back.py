list = str(input()).split(", ")
list_out = []

for i in range(len(list) -1, -1, -1):
    if int(list[i]) == 0:
        list_out.append(int(list[i]))
    else:
        list_out.insert(0,int(list[i]))
print(list_out)


