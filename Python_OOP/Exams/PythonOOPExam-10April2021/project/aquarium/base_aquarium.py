from abc import ABC
from project.fish.base_fish import BaseFish
from project.decoration.base_decoration import BaseDecoration
from project.common_functions import exc

class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: BaseFish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if fish.fish_type() in ["FreshwaterFish","SaltwaterFish"]:
            self.fish.append(fish)
            return f"Successfully added {fish.fish_type()} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        try:
            self.fish.remove(fish)
        except:
            pass

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        set(map(lambda fish: fish.eat(), self.fish))

    def __str__(self):
        fish = ' '.join(fish.name for fish in self.fish) if self.fish else "none"
        return f"""{self.name}:\nFish: {fish}\nDecorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"""


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Aquarium name cannot be an empty string.",not name)
        self.__name = name