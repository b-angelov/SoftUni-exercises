from abc import ABC, abstractmethod
from project.my_decorators import MyDecoratorsMxn as mdxn
from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: [BaseEquipment] = []

    @abstractmethod
    def win(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    @mdxn.check_str("Team name cannot be empty!")
    def name(self, value):
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    @mdxn.check_result_int("Advantage must be greater than zero!",0,"le")
    def advantage(self, value):
        self.__advantage = value

    def get_statistics(self):
        return f"Name: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Advantage: {self.advantage} points\n" \
               f"Budget: {self.budget:.2f}EUR\n" \
               f"Wins: {self.wins}\n" \
               f"Total Equipment Price: {sum(eq.price for eq in self.equipment):.2f}\n" \
               f"Average Protection: {int(sum(eq.protection for eq in self.equipment) / len(self.equipment)) if self.equipment else 0}"

    @property
    def team_score(self):
        return self.advantage + sum(eq.protection for eq in self.equipment)
