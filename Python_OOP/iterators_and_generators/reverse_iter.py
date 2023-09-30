
class reverse_iter:

    def __init__(self,iterable):
        self.iterable = iterable
        self.start = 0
        self.end = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.end < self.start:
            raise StopIteration
        else:
            end = self.end
            self.end -= 1
            return self.iterable[end]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
