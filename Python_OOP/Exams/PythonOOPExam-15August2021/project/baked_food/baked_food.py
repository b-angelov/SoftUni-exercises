from abc import ABC
from project.common_functions import exc

class BakedFood(ABC):

    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Name cannot be empty string or white space!", not name.strip())
        self.__name = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        exc("Price cannot be less than or equal to zero!",price <= 0)
        self.__price = price