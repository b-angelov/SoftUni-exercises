length = int(input())
width = int(input())
height = int(input())
used_space_percent = float(input()) / 100
space = round((length * width * height))
space /= 1000
space *= 1 - used_space_percent

print(space)