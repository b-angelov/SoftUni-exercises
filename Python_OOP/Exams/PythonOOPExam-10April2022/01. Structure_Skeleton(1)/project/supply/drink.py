from project.supply.supply import Supply,exc
# from supply import Supply

class Drink(Supply):

    def __init__(self, name: str):
        self.exc = exc
        self.energy = 15
        self.name = name
        self.supply_name = self.__class__.__name__

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
