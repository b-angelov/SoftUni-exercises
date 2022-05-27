number_of_orders = int(input())
total = 0

for i in range(number_of_orders):
    price_per_capsule = float(input()) #0.01 / 100.00
    days = int(input()) # 1 / 31
    capsules_count = int(input()) # 1 / 2000
    if not 0.01 <= price_per_capsule <= 100.00\
            or not 1 <= days <= 31\
            or not 1 <= capsules_count <= 2000:
        continue
    price = price_per_capsule * (capsules_count * days)
    '''if not price:
        continue
        pass'''
    print(f"The price for the coffee is: ${price:.2f}")
    total += price
    #price_per_capsule = days = capsules_count = price = 0

print(f"Total: ${total:.2f}")


