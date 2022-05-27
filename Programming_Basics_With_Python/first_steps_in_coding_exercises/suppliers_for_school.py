pens = int(input())
markers = int(input())
liters_detergent = int(input())
discount = int(input())
pens *= 5.80
markers *= 7.20
liters_detergent *= 1.20
result = (pens + markers + liters_detergent)
result -= result * (discount / 100)
print(result)



