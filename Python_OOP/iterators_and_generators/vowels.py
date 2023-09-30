
class vowels:

    def __init__(self, text: str):
        self.text = text
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.text):
            raise  StopIteration
        else:
            start = self.start
            self.start += 1
            if self.text[start] in "aeiuyoAEIUYO":
                return self.text[start]
            return self.__next__()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


