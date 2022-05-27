kicked_list = input().split(" ") # A-1/11 B-1/11
A = set("1 2 3 4 5 6 7 8 9 10 11".split(" "))
B = set("1 2 3 4 5 6 7 8 9 10 11".split(" "))
termin = ""

for kicked in kicked_list:
    kicked = kicked.split("-")
    team = kicked[0]
    num = kicked[1]
    if team == "A":
        A.discard(num)
    elif team == "B":
        B.discard(num)
    if len(A) < 7 or len(B) < 7:
        print(f"Team A - {len(A)}; Team B - {len(B)}\nGame was terminated")
        break
else:
    print(f"Team A - {len(A)}; Team B - {len(B)}")



