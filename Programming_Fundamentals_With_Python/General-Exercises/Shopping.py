budget = int(input())
end = ""

while end != "End":
    end = input()
    if end == "End":
        continue
    budget -= int(end)
    if budget < 0:
        print("You went in overdraft!")
        break
else:
    print("You bought everything needed.")
