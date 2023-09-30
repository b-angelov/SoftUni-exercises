from abc import ABC, abstractmethod


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0.0
        self.is_reserved = False

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self._capacity = value

    @property
    def is_reserved(self):
        return self._is_reserved

    @is_reserved.setter
    def is_reserved(self, value: float):
        if value == False:
            self.price_for_reservation = 0.0
            self._is_reserved = False
        else:
            self._is_reserved = True
            self.price_for_reservation = value
