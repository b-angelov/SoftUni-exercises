age = int(input())
drink = "whisky"

if age <= 14:
    drink = "toddy"
elif age <= 18:
    drink = "coke"
elif age <= 21:
    drink = "beer"
else:
    pass
'''

match age:
    case age if age <= 14:
        drink = "toddy"
    case age if age <= 18:
        drink = "coke"
    case age if age <= 21:
        drink = "beer"
    case _:
        pass
'''

print(f"drink {drink}")
