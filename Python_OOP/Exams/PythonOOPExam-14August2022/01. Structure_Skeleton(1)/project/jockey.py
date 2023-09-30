
class Jockey:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Name should contain at least one character!")
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age: int):
        if age < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
        self._age = age
