def even_odd(*args):
    condition = {"even": lambda a: not (int(a) % 2),"odd": lambda a: bool(int(a) % 2)}.get(args[-1],lambda: None)
    return list(filter(condition, args[:-1]))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))