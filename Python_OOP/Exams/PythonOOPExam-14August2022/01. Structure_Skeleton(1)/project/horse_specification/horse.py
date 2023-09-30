from abc import ABC, abstractmethod, abstractproperty

class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.add = 0
        self.is_taken = False
        self.rider = None


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if len(name) < 4:
            raise ValueError(f"Horse name {name} is less than 4 symbols!")
        self._name = name

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed: int):
        if speed > self.horse_max_speed and not self.speed:
            raise ValueError("Horse speed is too high!")
        elif speed > self.horse_max_speed:
            speed = self.horse_max_speed
        self._speed = speed

    @property
    def is_taken(self):
        return self._is_taken
    @is_taken.setter
    def is_taken(self, value):
        if value:
            self.rider = value
            self._is_taken = True
        else:
            self._is_taken = False
            self.rider = None

    @abstractmethod
    def train(self):
        self.speed += self.add