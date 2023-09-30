from abc import ABC
from project.common_functions import exc

class Drink(ABC):

    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        exc("Name cannot be empty string or white space!", not name.strip())
        self.__name = name

    @property
    def portion(self):
        return self.__portion
    @portion.setter
    def portion(self, portion: float):
        exc("Portion cannot be less than or equal to zero!",portion <= 0)
        self.__portion = portion

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        exc("Brand cannot be empty string or white space!",not brand.strip())
        self.__brand = brand

