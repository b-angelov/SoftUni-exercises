class lst:

    def __init__(self):
        self.__last_index = -1

    def __len__(self):
        return self.__last_index + 1

    def __setitem__(self, key, value):
        key = self.__validate_index(key)
        self.__dict__[key] = value

    def __getitem__(self, item):
        item = self.__validate_index(item)
        return self.__dict__[item]

    def __delitem__(self, item):
        item = self.__validate_index(item)
        del self.__dict__[item]
        self.__reorder_list()

    def __iter__(self):
        return next(self)

    def __next__(self):
        index = 0
        while index in self.__dict__:
            yield self.__dict__[index]
            index += 1

    def __repr__(self):
        return f"[" + ', '.join(str(i) for i in self) + "]"

    def __deleted(self):
        pass

    def __validate_index(self, index):
        if index < 0:
            index = len(self) + index
        if type(self.__dict__.get(index, self.__deleted)) == self.__deleted:
            raise IndexError("Index out of lst range.")
        return index

    def __reorder_list(self):
        trim = self.__last_index + 1
        dci = 0
        for i in range(0, self.__last_index + 1):
            try:
                if self[i] != self.__deleted:
                    self[dci] = self[i]
                    dci += 1
                else:
                    # print(trim, self.__last_index, self.__deleted)
                    trim -= 1
                    # print(trim, self.__last_index, self.__deleted)
            except:
                pass

        for i in range(trim, self.__last_index + 1):
            try:
                del self[i]
            except:
                pass
        self.__last_index = trim - 1

    def append(self, value):
        self.__dict__[self.__last_index + 1] = value
        self.__last_index += 1
        return self

    def remove(self, index):
        index = self.__validate_index(index)
        val = self[index]
        self[index] = self.__deleted
        self.__reorder_list()
        return val

    def get(self, index):
        return self[index]

    def extend(self, iterable):
        for i in iterable:
            self.append(i)
        return self

    def insert(self, index, value):
        index = self.__validate_index(index)
        idx = 0
        while idx in range(len(self) + 1):
            if idx == index:
                tmp = self[index]
                self[index] = value
            if idx > index:
                t = self[idx] if idx < len(self) else None
                self.__dict__[idx] = tmp
                tmp = t
            idx += 1
        self.__last_index += 1
        return self

    def pop(self, idx=None):
        if idx is None:
            idx = self.__last_index
        idx = self.__validate_index(idx)
        v = self.__dict__[idx]
        self[idx] = self.__deleted
        self.__reorder_list()
        return v

    def clear(self):
        idx = 0
        while idx <= self.__last_index:
            del self[idx]
            idx += 1
        self.__last_index = -1

    def index(self, value):
        # self.__validate_index(index)
        # return self.__dict__[index]
        for i in range(len(self)):
            if self[i] == value:
                return i

    def count(self, value):
        n = 0
        for i in self:
            if i == value:
                n += 1
        return n

    def reverse(self):
        new = lst()
        start, end = self.__last_index, 0
        while start >= end:
            new.append(self.get(start))
            start -= 1
        return new

    def copy(self):
        new = lst()
        for i in self:
            new.append(i)
        return new

    def size(self):
        return len(self)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        return {self[k]: self[k + 1] if k + 1 in range(len(self)) else " " for k in range(0, len(self), 2)}

    def move(self, amount):
        lst = [self.pop(0) for _ in range(amount)]
        self.extend(lst)
        return lst

    def sum(self):
        return sum(i if isinstance(i, (int, float)) else len(i) for i in self)

    def overbound(self):
        return self.index(max(self, key=lambda x: x if isinstance(x, (int, float)) else len(x)))

    def underbound(self):
        return self.index(min(self, key=lambda x: x if isinstance(x, (int, float)) else len(x)))


if __name__ == "__main__":
    my_lst = lst()
    # my_lst.append("aaaaa")
    # my_lst.extend(["a",5,8,"opooop"])
    # print(my_lst.dictionize())
    # print(my_lst.move(2))
    # print(my_lst.sum())
    # print(my_lst.overbound())
    # print(my_lst.underbound())
    # print(my_lst)
    # my_lst.remove(2)
    # print(my_lst)
    # my_lst.remove(1)
    # print(my_lst)
    # my_lst.remove(0)
    # print(my_lst)
    # my_lst.remove(0)
    # print(len(my_lst),my_lst.pop(0), my_lst)

    my_lst.append("A")
    my_lst.append("B")
    my_lst.append("C")
    print(my_lst)
    my_lst.remove(2)
    print(my_lst)
    my_lst.remove(0)
    print(my_lst)
    my_lst.extend(("A", "C"))
    print(my_lst)
    my_lst.insert(0, "A")
    my_lst.insert(2, "C")
    my_lst.insert(4, "B")
    print(my_lst, "here")
    my_lst.pop()
    print(my_lst)
    my_lst.pop(-2)
    print(my_lst)
    my_lst.pop(-1)
    print(my_lst)
    print(my_lst.clear())
    print(my_lst)
    my_lst.extend(tuple("ABC"))
    print(my_lst)
    print(my_lst.index("C"))
    print(my_lst.count("E"))
    print(my_lst.count("A"))
    print(my_lst.count("AB"))
    print(my_lst.reverse())
    new_lst = my_lst.copy()
    print(new_lst, my_lst == new_lst)
    print(my_lst.size())
    my_lst.add_first("Y")
    print(my_lst, new_lst)
    print(my_lst.dictionize())
    print(new_lst.dictionize())
    my_lst.move(2)
    print(my_lst)
    print(my_lst.sum())
    print(my_lst.overbound())
    my_lst.append("abc")
    print(my_lst.overbound())
    print(my_lst.underbound())
    print(len(my_lst))
    my_lst.insert(3,"")
    print(my_lst)
    print(my_lst.underbound())