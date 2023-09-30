even,odd = set(),set()
for i in range(1,int(input())+1):
    n = sum(ord(c) for c in input()) // i
    if n % 2:
        odd.add(n)
    else:
        even.add(n)
even_sum,odd_sum = sum(even),sum(odd)

if even_sum == odd_sum:
    print(", ".join(str(c) for c in odd|even))
elif odd_sum > even_sum:
    print(", ".join(str(c) for c in odd-even))
if even_sum > odd_sum:
    print(", ".join(str(c) for c in odd^even))