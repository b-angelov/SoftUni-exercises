inp = ""

while inp != "End":
    inp = str(input())
    if inp == "SoftUni" or inp == "End":
        continue
    for i in range(0, len(inp)):
        print(f"{inp[i]}{inp[i]}", end="")
    print()