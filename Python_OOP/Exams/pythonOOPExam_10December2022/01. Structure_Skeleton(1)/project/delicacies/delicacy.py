from abc import ABC, abstractmethod


class Delicacy(ABC):

    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if name.strip() == "":
            raise ValueError("Name cannot be null or whitespace!")
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            raise ValueError("Price cannot be less or equal to zero!")
        self._price = price

    @abstractmethod
    def details(self):
        ...
