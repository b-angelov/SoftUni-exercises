from abc import ABC, abstractmethod


class BaseEquipment(ABC):

    def __init__(self, protection: int, price: float):
        self.price = price
        self.protection = protection

    @abstractmethod
    def increase_price(self):
        pass
