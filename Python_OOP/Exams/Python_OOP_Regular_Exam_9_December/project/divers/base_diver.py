from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: [BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self, ):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
            return
        self.oxygen_level -= fish.time_to_catch
        self.competition_points += fish.points
        self.catch.append(fish)

    def update_health_status(self, ):
        self.has_health_issue = not self.has_health_issue

    def __str__(self, ):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return self.__competition_points

    @competition_points.setter
    def competition_points(self, value):
        self.__competition_points = round(float(value), 1)
