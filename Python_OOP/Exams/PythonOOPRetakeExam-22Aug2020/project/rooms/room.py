from abc import ABC, abstractmethod

class Room(ABC):

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0

    def calculate_expenses(self,*args):
        value = 0
        for el in args:
            # for elem in arg:
            for arg in el:
                try:
                    value += arg.get_monthly_expense()
                except:
                    value += arg.cost * 30
        self.expenses = value

    @property
    def expenses(self):
        return self.__expenses
    @expenses.setter
    def expenses(self, expenses: float):
        if expenses < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = expenses