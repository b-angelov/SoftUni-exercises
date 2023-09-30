from abc import ABC, abstractmethod

def raise_exception(function):
    def e_raise(message, condition, error=ValueError):
        if function(condition):
            raise error(message)

    return e_raise


@raise_exception
def exc(cond):
    if cond: return True

class Supply(ABC):

    def __init__(self, name: str, energy: int):
        self.exc = exc
        self.name = name
        self.energy = energy

    @abstractmethod
    def details(self):
        """Return the supply's type, name and energy in the format: "{type}: {name}, {energy}".
The type of the supply is either "Food" or "Drink".
Hint: override the method in the child classes.
"""
        ...

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name:str):
        self.exc("Name cannot be an empty string.",not name)
        self._name = name

    @property
    def energy(self):
        return self._energy
    @energy.setter
    def energy(self, energy: int):
        self.exc("Energy cannot be less than zero.",energy < 0)
        self._energy = energy
