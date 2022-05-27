processor_in_dollars = float(input())  #  200.00/3000.00
graphics_card_in_dillars = float(input())  #  100.00/1500.00
single_RAM_in_dollars = float(input())  #  80.00/500.00
RAM_count = int(input())  #  1/4
discount_percent = float(input())  # 0.01/0.1

result = (processor_in_dollars + graphics_card_in_dillars) * ( 1 - discount_percent) + (single_RAM_in_dollars * RAM_count)
result *= 1.57
print(f"Money needed - {result:.2f} leva.")

# Money needed - {общо лева} leva.
