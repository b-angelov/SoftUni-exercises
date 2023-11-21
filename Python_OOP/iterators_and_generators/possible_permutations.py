###Workaround Solution ####

def possible_permutations(lst: list):
    for i,v in enumerate(lst):
        yield [v] + [lst[x] for x in range(len(lst)) if x != i]
        if len(lst) == 1:
            raise StopIteration
        yield [v] + [lst[x] for x in range(len(lst) - 1,-1,-1) if x != i]
 

### Acceptable Solution###

def possible_permutations(lst):
    if len(lst) < 2:
        yield lst
        return
    for i in range(len(lst)):
        for el in possible_permutations(lst[:i] + lst[i+1:]):
            yield [lst[i]] + el
 

[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]
