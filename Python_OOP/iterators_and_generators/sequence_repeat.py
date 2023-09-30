class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = str(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.__i
        except:
            self.__i = 0
        if self.__i == self.number:
            raise StopIteration
        idx = self.__i % len(self.sequence)
        self.__i += 1
        return self.sequence[idx]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

