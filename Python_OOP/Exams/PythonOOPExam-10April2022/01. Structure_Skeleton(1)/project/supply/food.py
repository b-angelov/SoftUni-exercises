from project.supply.supply import Supply,exc
# from supply import Supply

class Food(Supply):

    def __init__(self, name: str, energy: int = 25):
        self.exc = exc
        self.name = name
        self.energy = energy
        self.supply_name = self.__class__.__name__

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"

