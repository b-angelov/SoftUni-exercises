groups = int(input())
musala = monblan = kilimanjaro = k2 = everest = all = 0

for i in range(1, groups + 1):
    members = int(input())
    all += members

    if members <= 5:
        musala += members
    elif 5 < members <= 12:
        monblan += members
    elif 12 < members <= 25:
        kilimanjaro += members
    elif 25 < members <= 40:
        k2 += members
    else:
        everest += members

print(f"{(musala / all) * 100:.2f}%\n{(monblan / all) * 100:.2f}%\n{(kilimanjaro / all) * 100:.2f}%\n{(k2 / all) * 100:.2f}%\n{(everest / all) * 100:.2f}%")
