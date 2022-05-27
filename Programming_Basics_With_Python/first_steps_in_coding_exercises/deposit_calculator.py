ammount = float(input())
months = int(input())
interest = float(input()) / 100
total = ammount + months * ((ammount * interest) /12)
print(total)