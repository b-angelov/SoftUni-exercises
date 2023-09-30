
class custom_range:

    def __init__(self,start:int,end:int):
        self.start,self.end = start,end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            start = self.start
            self.start += 1
            return start


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
