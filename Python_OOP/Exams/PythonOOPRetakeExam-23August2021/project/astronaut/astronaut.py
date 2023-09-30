from abc import ABC,abstractmethod
from project.common_functions import exc


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
        self.default_breath_amount = 10

    @abstractmethod
    def breathe(self):
        """Each time an astronaut takes a breath, their oxygen decreases by 10 units. Note: some types of astronauts need more oxygen units while breathing."""
        ...

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def condition(self):
        return f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {', '.join(self.backpack) if self.backpack else 'none'}"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Astronaut name cannot be empty string or whitespace!", not name.strip())
        self.__name = name