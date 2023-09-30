from abc import ABC, abstractmethod

class Musician(ABC):

    def __init__(self,name: str,age : int ):
        self.name = name
        self.age = age
        self.skills = []

    @abstractmethod
    def learn_new_skill(self,new_skill: str):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name:str):
        if not name.strip():
            raise ValueError("Musician name cannot be empty!")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        if age < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self._age = age



