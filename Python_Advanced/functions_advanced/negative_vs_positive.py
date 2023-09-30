list = list(map(int,input().split()))
negatives = sum(i for i in list if i < 0)
positives = sum(i for i in list if i > 0)
print(
    negatives,
    positives,
    "The negatives are stronger than the positives"
    if abs(negatives)>positives else
    "The positives are stronger than the negatives",
    sep="\n"
)