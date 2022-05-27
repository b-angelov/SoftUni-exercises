n = ""
sum = 0
while True:
    inp = input()
    if str(inp) == "NoMoreMoney":
        break
    elif float(inp) >= 0:
        sum += float(inp)
        print(f"Increase: {float(inp):.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {sum:.2f}")