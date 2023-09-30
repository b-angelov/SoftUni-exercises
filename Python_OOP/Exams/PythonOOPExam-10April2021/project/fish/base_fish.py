from abc import ABC, abstractmethod
from project.common_functions import exc

class BaseFish(ABC):
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price
        self.habitat = "Any"

    @abstractmethod
    def eat(self):
        self.size += 5

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Fish name cannot be an empty string.",not name)
        self.__name = name

    @property
    def species(self):
        return self.__species
    @species.setter
    def species(self, species: str):
        exc("Fish species cannot be an empty string.",not species)
        self.__species = species

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        exc("Price cannot be equal to or below zero.",price <= 0)
        self.__price = price

    def fish_type(self):
        return self.__class__.__name__