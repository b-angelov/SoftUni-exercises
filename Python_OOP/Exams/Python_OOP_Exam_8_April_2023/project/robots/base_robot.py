from abc import ABC, abstractmethod


class BaseRobot(ABC):

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight


    @abstractmethod
    def eating(self):
        """The method increases the robot's kilograms"""
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Robot name cannot be empty!")
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        if not kind.strip():
            raise ValueError("Robot kind cannot be empty!")
        self.__kind = kind

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
        if 0.0 >= price:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")


