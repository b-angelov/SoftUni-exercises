from abc import ABC, abstractmethod
from project.helper import string_is_empty,value_in_inclusive_range


class BaseFish(ABC):

    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch  # in seconds

    @abstractmethod
    def fish_details(self):
        pass

    def _display_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"

    @property
    def name(self):
        return self.__name

    @name.setter
    @string_is_empty("Fish name should be determined!")
    def name(self, value):
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    @value_in_inclusive_range(1, 10, "Points should be a value ranging from 1 to 10!")
    def points(self, value):
        self.__points = value
