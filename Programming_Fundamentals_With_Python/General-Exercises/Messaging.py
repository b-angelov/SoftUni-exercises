lis = str(input()).split(" ")
stri = list(input())
str_len = len(stri)
message = ""

for a in lis:
    num_list = list(a)
    num_list = [int(i) for i in num_list]
    index = sum(num_list)
    difference = index // str_len
    if difference >= 1:
        index -= str_len * difference
    message += stri[index]
    del stri[index]
print(message)