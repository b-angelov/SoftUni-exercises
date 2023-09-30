from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    @abstractmethod
    def make_sound(cls):
        ...

    @abstractmethod
    def __repr__(self):
        ...
