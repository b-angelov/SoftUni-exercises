score = int(input())

if score <= 100:
    bonus = 5
else:
    if score <= 1000:
        bonus = score * 0.20
    else:
        bonus = score * 0.10

if score % 2 == 0 :
    extra = 1
elif score % 5 == 0 :
    extra = 2
else:
    extra = 0

print(bonus + extra)
print(bonus + score + extra)