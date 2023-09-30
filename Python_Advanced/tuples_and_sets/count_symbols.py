strng = input()
print(*(f"{c}: {strng.count(c)} time/s" for c in sorted(set(strng))),sep="\n")