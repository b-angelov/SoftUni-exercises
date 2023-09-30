from project.common_functions import exc

class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Name cannot be an empty string!",not name)
        self.__name = name
