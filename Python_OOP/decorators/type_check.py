def type_check(type_):
    def ins(func):
        def inner(*args):
            if type(args[0]) != type_:
                return "Bad Type"
            return func(*args)
        return inner
    return ins

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


