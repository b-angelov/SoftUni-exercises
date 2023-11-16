from abc import ABC, abstractmethod
from project.loans.base_loan import BaseLoan


class BaseClient(ABC):

    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest = interest
        self.loans: [BaseLoan] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__clid

    @client_id.setter
    def client_id(self, value):
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__clid = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        self.__income = value
        if self.__income <= 0.0:
            raise ValueError("Income must be greater than zero!")

    @abstractmethod
    def increase_clients_interest(self):
        ...

    def _increase_interest(self, amount: float):
        self.interest += amount

    def __add__(self, other):
        other = other.income if isinstance(other, self.__class__) else other
        return self.income + other.income
