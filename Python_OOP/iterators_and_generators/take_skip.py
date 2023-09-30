class take_skip:

    def __init__(self, step:int, count:int):
        self.step = step
        self.count = count
        self.__i = 0
        self.__sum = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i >= self.count:
            raise StopIteration
        self.__i += 1
        count = self.__sum
        self.__sum += self.step
        return count


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

