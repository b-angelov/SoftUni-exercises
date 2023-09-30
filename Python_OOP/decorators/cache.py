def cache(func):
    log = {}
    def inner(n):
        res = func(n)
        log[n] = res
        return res
    inner.log = log
    return inner


@cache
def fibonacci(n):
    if n < 2:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)

