class HashTable:

    DEFAULT_TABLE_LENGTH = 4

    def __init__(self):
        self.__table_length = self.DEFAULT_TABLE_LENGTH
        self.__array = [None for _ in range(self.DEFAULT_TABLE_LENGTH)]

    def __len__(self):
        return len(self.__array)

    @property
    def array(self):
        return self.__array

    # @property
    # def __append_array(self):
    #     return self.__array
    #
    # @__append_array.setter
    # def __append_array(self, value):
    #     if not isinstance(value, (tuple,list)) or len(value) != 2:
    #         raise ValueError("Given values are not supported with hash table.")
    #     if len(self.__array) % (self.DEFAULT_TABLE_LENGTH + 1) == self.DEFAULT_TABLE_LENGTH:
    #         self.__array.extend(None for _ in range(len(self.__array)))
    #     first_available_index = next((idx for idx,val in enumerate(self.__array) if val is None))
    #     self.__array[first_available_index] = tuple(value)

    def hash(self, key):
        try:
            first_available_index = next((idx for idx,val in enumerate(self.__array) if val is None or val[0] == key))
        except StopIteration:
            if len(self.__array) > self.DEFAULT_TABLE_LENGTH:
                pass
            self.__array.extend(None for _ in range(len(self.__array)))
            first_available_index = next((idx for idx,val in enumerate(self.__array) if val is None or val[0] == key))
        slot = [None,None]
        self.__array[first_available_index] = slot
        return slot

    def add(self, key: str, value: any):
        slot = self.hash(key)
        slot[0] = key
        slot[1] = value

    def get(self, key: str):
        try:
            value = next(value for k,value in self.__array if k == key)
        except IndexError:
            raise KeyError("Provided key does not exist in the hash table.")
        except TypeError:
            raise StopIteration
        return value

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __delitem__(self, key):
        item = next((i for i in self.__array if i and i[0] == key), None)
        if item:
            self.__array.remove(item)
        return item

    def __iter__(self):
        return next(self)

    def __next__(self):
        index = 0
        while True:
            if index >= len(self.__array) or self.__array[index] is None:
                index = 0
                return
            yield self.__array[index][0]
            index += 1

    def __add__(self, other):
        res = HashTable()
        [res.add(r[0],r[1]) for i in [self.__array, other.array] for r in i if r]
        return res

    # this has been commented out due to task result restrictions
    def __repr__(self):
        return '{' + ', '.join(f"{res[0]}: {res[1]}" for res in self.array if res) + '}'

    def __bool__(self):
        return any(self.__array)





if __name__ == "__main__":
    table = HashTable()

    table["name"] = "Peter"
    table["age"] = 25

    print(table)
    print(table.get("name"))
    print(table["age"])
    print(len(table))

