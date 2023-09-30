def vowel_filter(function):

    def wrapper():

        return list(filter(lambda x: x in "aeiouy",function()))

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
