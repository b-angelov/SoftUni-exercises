def fibonacci():
    prev = 1
    yield 0
    yield 1
    next = 1
    while True:
        i = next
        yield next
        next += prev
        prev = i

generator = fibonacci()
for i in range(12):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))

