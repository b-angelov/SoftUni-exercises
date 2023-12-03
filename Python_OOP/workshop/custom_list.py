
class lst:

    def __init__(self):
        self.__last_index = -1

    def append(self, value):
        self.__dict__[self.__last_index + 1] = value
        self.__last_index += 1
        return self

    def remove(self, index):
        self.__validate_index(index)
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
        self.__validate_index(index)
        idx = 0
        while idx in self.__dict__ and idx < self.__last_index:
            if idx == index:
                tmp = self.__dict__[index]
                self.__dict__[index] = value
            if idx > index:
                t = self.__dict__[index]
                self.__dict__[index] = tmp
                tmp = t
            index += 1
        return self

    def pop(self, idx = None):
        if idx is None:
            idx = self.__last_index
        self.__validate_index(idx)
        v = self.__dict__[idx]
        self[idx] = self.__deleted
        self.__reorder_list()
        return v

    def clear(self):
        idx = 0
        while idx <= self.__last_index:
            del self[idx]

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
        start,end = self.__last_index, 0
        while start >= end:
            new.append(self.get(start))
        return new

    def copy(self):
        new = lst()
        for i in self:
            new.append(i)
        return new

    def __deleted(self):
        pass


    def __len__(self):
        return self.__last_index + 1

    def __validate_index(self, index):
        if not self.__dict__.get(index, None):
            raise IndexError("Index out of lst range.")

    def __reorder_list(self):
        trim = self.__last_index + 1
        dci = 0
        for i in range(0,self.__last_index+1):
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

        for i in range(trim,self.__last_index+1):
            try:
                del self[i]
            except:
                pass
        self.__last_index = trim - 1


    def __setitem__(self, key, value):
        self.__validate_index(key)
        self.__dict__[key] = value

    def __getitem__(self, item):
        self.__validate_index(item)
        return self.__dict__[item]

    def __delitem__(self, item):
        self.__validate_index(item)
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

    def size(self):
        return len(self)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        return {self[k]:self[k+1] if k+1 in range(len(self)) else " " for k in range(0,len(self),2)}

    def move(self, amount):
        lst = [self.pop(l) for l in range(amount)]
        self.extend(lst)
        return lst

    def sum(self):
        return sum(i if isinstance(i, (int,float)) else len(i) for i in self)

    def overbound(self):
        return self.index(max(self, key=lambda x: x if isinstance(x,(int,float)) else len(x)))

    def underbound(self):
        return self.index(min(self, key=lambda x: x if isinstance(x,(int,float)) else len(x)))


if __name__ == "__main__":
    my_lst = lst()
    my_lst.append("aaaaa")
    my_lst.extend(["a",5,8,"opooop"])
    print(my_lst.dictionize())
    print(my_lst.move(2))
    print(my_lst.sum())
    print(my_lst.overbound())
    print(my_lst.underbound())
    print(my_lst)
    my_lst.remove(2)
    print(my_lst)
    my_lst.remove(1)
    print(my_lst)
    my_lst.remove(0)
    print(my_lst)
    my_lst.remove(0)
    print(len(my_lst),my_lst.pop(0), my_lst)




