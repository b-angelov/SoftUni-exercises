class HashTable:

    DEFAULT_TABLE_LENGTH = 4

    def __init__(self):
        self.__array = [None for _ in range(self.DEFAULT_TABLE_LENGTH)]
        self.__keys = []

    def __len__(self):
        return len(self.__array)

    def __none(self):
        return None

    @property
    def array(self):
        return tuple(self.__array)

    @property
    def keys(self):
        return tuple(self.__keys)

    def hash(self, key):
        first_available_index = self.__get_next_index()
        hash_value = str(hash(key))
        self.__setattr__(hash_value, first_available_index)
        self.__keys.append(key)
        return hash_value, first_available_index

    def add(self, key: str, value: any):
        try:
            index = self.__getattribute__(str(hash(key)))
        except AttributeError:
            index = self.hash(key)[1]
        self.__array[index] = value if value is not None else self.__none

    def get(self, key: str, default_value=KeyError, error_message = ""):
        if not error_message:
            error_message = f"Key '{key}' not found in hash table."
        try:
            result = self.__getattribute__(str(hash(key)))
        except AttributeError:
            if callable(default_value) and isinstance(default_value(), BaseException):
                raise default_value(error_message)
            return default_value
        result = self.__array[result]
        if result == self.__none:
            result = result()
        return result



    def __get_next_index(self):
        try:
            next_index = next(index for index in range(len(self.__array)) if self.__array[index] is None)
        except StopIteration:
            self.__array.extend(None for _ in range(len(self.__array)))
            next_index = self.__get_next_index()
        return next_index

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        hash_value = str(hash(key))
        try:
            index = self.__getattribute__(hash_value)
        except AttributeError:
            raise KeyError("Key doesn't exist in hash table.")
        self.__array[index] = None
        self.__keys.remove(key)
        self.__delattr__(hash_value)

    def __iter__(self):
        return next(self)

    def __next__(self):
        for key in self.__keys:
            yield self.get(key)
        # while True:
        #     for key in self.__keys:
        #         yield self.get(key)
        #     else:
        #         return

    def __add__(self, other):
        result = HashTable()
        set(result.add(key if not result.get(key,None) else f"{key} second", i.get(key))
            for i in [self, other] for key in i.keys if key)
        return result

    def __bool__(self):
        return bool(self.keys)

    def __str__(self):
        return str(type(self))

    def __repr__(self):
        return "{" + ', '.join(f'{key}: {self.get(key)}' for key in self.__keys) + "}"



if __name__ == "__main__":
    table = HashTable()

    table["name"] = "Peter"
    table["age"] = 25

    print(table)
    print(table.get("name"))
    print(table["age"])
    print(len(table))

