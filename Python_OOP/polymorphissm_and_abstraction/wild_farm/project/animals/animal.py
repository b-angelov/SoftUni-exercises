from abc import ABC, abstractmethod
from project.food import Vegetable, Fruit, Meat, Seed, Food


class Animal(ABC):
    food = ["Vegetable","Fruit","Meat","Seed"]
    food_increase_rate = 0
    sound = ""

    def __init__(self, name: str, weight: float):
        self.food_eaten = 0
        self.name = name
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        return self.sound

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += self.food_increase_rate * food.quantity


class Bird(Animal):


    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def make_sound(self):
        return self.sound

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def make_sound(self):
        return self.sound

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
