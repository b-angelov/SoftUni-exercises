from project.common_functions import exc

class Planet:

    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Planet name cannot be empty string or whitespace!",not name.strip())
        self.__name = name