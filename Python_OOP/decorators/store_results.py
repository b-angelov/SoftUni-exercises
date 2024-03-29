class store_results:

    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        with open("result.txt", "a") as file:
            file.write(f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}\n")
            file.close()


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
