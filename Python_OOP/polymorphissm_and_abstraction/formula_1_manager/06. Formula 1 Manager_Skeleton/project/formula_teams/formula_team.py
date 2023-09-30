from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        ...

    @staticmethod
    def sponsor_funds(race_pos, items):
        res = list(filter(lambda x: x[0] >= race_pos, items))
        return  min(res, key=lambda x: x[0])[1] if res else 0
