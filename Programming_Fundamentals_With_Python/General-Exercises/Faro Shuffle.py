cards = input().split(" ")
count_shuffles = int(input())
for _ in range(count_shuffles):
    half = len(cards) // 2
    first = cards[:half]
    second = cards[half:]
    out = []

    for card in range(half):
        out.append(first[card])
        out.append(second[card])
    cards = out
print(cards)
