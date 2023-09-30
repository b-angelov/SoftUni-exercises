from project.animals.animal import Mammal


class Mouse(Mammal):
    sound = "Squeak"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food = [self.food[0], self.food[1]]
        self.food_increase_rate = 0.10



class Dog(Mammal):
    sound = "Woof!"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food = [self.food[2]]
        self.food_increase_rate = 0.40



class Cat(Mammal):
    sound = "Meow"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food = [self.food[0], self.food[2]]
        self.food_increase_rate = 0.30



class Tiger(Mammal):
    sound = "ROAR!!!"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food = [self.food[2]]
        self.food_increase_rate = 1.00

