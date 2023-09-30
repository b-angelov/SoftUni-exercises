from project.common_functions import exc

class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Name should contain at least one character!",not name.strip())
        self.__name = name