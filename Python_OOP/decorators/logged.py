
def logged(func):
    def inner(*args):
        res = f"you called {func.__name__}({', '.join(map(str,args))})"
        res +=f"\nit returned {func(*args)}"
        return res
    return inner


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

