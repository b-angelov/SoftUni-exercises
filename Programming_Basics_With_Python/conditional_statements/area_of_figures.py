from math import pi

print("figure type:")
figure = str(input())
print("parameters:")
a = float(input())

if figure == "rectangle" or figure == "triangle":
    b = float(input())

if figure == "square":
    print(a*a)
elif figure == "rectangle":
    print(a*b)
elif figure == "circle":
    print((a*a)*pi)
elif figure == "triangle":
    print((a*b)/2)