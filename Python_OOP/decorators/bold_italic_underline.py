def make_bold(func):
    def inner(*args):
        return f"<b>{func(*args)}</b>"
    return inner


def make_italic(func):
    def inner(*args):
        return f"<i>{func(*args)}</i>"
    return inner

def make_underline(func):
    def inner(*args):
        return f"<u>{func(*args)}</u>"
    return inner

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
