from abc import ABC, abstractmethod
from project.common_functions import exc

class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.__owner = None
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False
    @property
    @abstractmethod
    def min_speed_limit(self):
        ...
    @property
    @abstractmethod
    def max_speed_limit(self):
        ...


    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        exc(f"Model {model} is less than 4 symbols!", len(model) < 4)
        self.__model = model

    @property
    def speed_limit(self):
        return self.__speed_limit
    @speed_limit.setter
    def speed_limit(self, speed_limit: int):
        exc(f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!", speed_limit not in range (self.min_speed_limit,self.max_speed_limit+1))
        self.__speed_limit = speed_limit

    @property
    def is_taken(self):
        return bool(self.__owner)
    @is_taken.setter
    def is_taken(self, owner: object):
        self.__owner = owner

    @property
    def car_type(self):
        return self.__class__.__name__


