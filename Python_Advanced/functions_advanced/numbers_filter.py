def even_odd_filter(**kwargs):
    conditions = {"even": lambda a: not (int(a) % 2), "odd": lambda a: bool(int(a) % 2)}
    result = {}
    for key,values_list in kwargs.items():
        condition = conditions.get(key)
        result[key] = list(filter(condition,values_list))
    return result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
