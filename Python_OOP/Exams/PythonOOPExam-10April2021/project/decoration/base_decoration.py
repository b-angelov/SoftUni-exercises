from abc import ABC, abstractmethod

class BaseDecoration(ABC):

    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price
        self.decoration_type = self.__class__.__name__