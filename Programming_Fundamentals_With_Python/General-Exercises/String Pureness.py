n = int(input())

for i in range(0, n):
    string = str(input())
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")