from abc import ABC, abstractmethod

class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be an empty string!")
        self._name = name

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price: float):
        if price <= 0:
            raise ValueError("Invalid price!")
        self._price = price

    @abstractmethod
    def details(self):
        ...
