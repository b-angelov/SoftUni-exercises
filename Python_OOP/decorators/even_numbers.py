def even_numbers(function):

    def wrapper(numbers):

        return list(filter(lambda x: not x % 2,function(numbers)))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
