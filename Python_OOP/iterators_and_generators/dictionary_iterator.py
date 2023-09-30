class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())

    def __iter__(self):
        return self



    def __next__(self):
        try:
            self.__item
        except:
            self.__item = 0
        if self.__item == len(self.dictionary):
            raise StopIteration
        item = self.dictionary[self.__item]
        self.__item += 1
        return item

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

