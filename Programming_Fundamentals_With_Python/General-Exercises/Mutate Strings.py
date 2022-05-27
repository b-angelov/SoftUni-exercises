str1 = list(input())
str2 = list(input())


for i in range(len(str2)):
    if str1[i] == str2[i]:
        continue
    str1[i] = str2[i]
    current = ''.join(str1)
    print(current)
