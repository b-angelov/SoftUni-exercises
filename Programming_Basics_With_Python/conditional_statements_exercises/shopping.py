budget = float(input())
quantity_graphic_cards = int(input())
quantity_processors = int(input())
quantity_RAM = int(input())
graphic_cards = quantity_graphic_cards * 250
processors = quantity_processors * (graphic_cards * 0.35)
ram = graphic_cards * (quantity_RAM * 0.10)
discount = 1.0
if quantity_graphic_cards > quantity_processors:
    discount = 0.85

result = (graphic_cards + processors + ram) * discount
if result <= budget:
    print(f"You have {budget - result:.2f} leva left!")
else:
    print(f"Not enough money! You need {result - budget:.2f} leva more!")