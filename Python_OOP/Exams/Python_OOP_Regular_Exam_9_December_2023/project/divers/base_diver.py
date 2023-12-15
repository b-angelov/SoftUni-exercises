from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish
from project.helper import *


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name: str = name
        self.oxygen_level: float = oxygen_level
        self.catch: list = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    def hit(self, fish: BaseFish):
        try:
            self.oxygen_level -= fish.time_to_catch
        except ValueError:
            self.oxygen_level = 0
        else:
            self.catch.append(fish)
            self.competition_points += round(fish.points, 1)
        if self.oxygen_level == 0:
            self.has_health_issue = True

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"

    def _miss(self, time_to_catch_:int, percentage):
        time_to_catch = round(time_to_catch_ * percentage)
        try:
            self.oxygen_level -= time_to_catch
        except ValueError:
            self.oxygen_level = 0
        if self.oxygen_level == 0:
            self.has_health_issue = True

    def _renew_oxygen(self, value):
        self.oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    @property
    def name(self):
        return self.__name


    @name.setter
    @string_is_empty("Diver name cannot be null or empty!")
    def name(self, value):
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    @is_below_zero("Cannot create diver with negative oxygen level!")
    def oxygen_level(self, value):
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return round(float(self.__competition_points), 1)

    @competition_points.setter
    def competition_points(self, value):
        self.__competition_points = value
