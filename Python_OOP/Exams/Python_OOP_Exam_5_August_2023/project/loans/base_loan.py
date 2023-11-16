from abc import ABC, abstractmethod


class BaseLoan(ABC):

    def __init__(self, interest_rate: float, amount: float):
        self.amount = amount
        self.interest_rate = interest_rate

    @abstractmethod
    def increase_interest_rate(self):
        ...

    def _increase_rate(self, amount: float):
        self.interest_rate += amount

    def __add__(self, other):
        return self.amount + other.amount
