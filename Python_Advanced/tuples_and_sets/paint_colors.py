from collections import deque

from math import ceil

string = deque(input().split())
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange": {"red", "yellow"}, "purple": {"red", 'blue'}, "green": {"yellow", "blue"}}
colors_found = []
chk = lambda word: word in main_colors or word in secondary_colors.keys()

while string:
    if len(string) > 1:
        first, last = string.popleft(), string.pop()
        if chk(first+last):
            colors_found.append(first+last)
        elif chk(last+first):
            colors_found.append(last+first)
        else:
            strln = len(string)
            if first[:-1]:
                string.insert(ceil(strln/2),first[:-1])
            if last[:-1]:
                string.insert(ceil(strln/2),last[:-1])
    else:
        word = string.pop()
        if chk(word):
            colors_found.append(word)

for color in colors_found:
    if color in secondary_colors.keys() and secondary_colors[color].intersection(colors_found) != secondary_colors[color]:
        colors_found.remove(color)
print(colors_found)

