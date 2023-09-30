from project.animals.animal import Bird


class Owl(Bird):
    sound = "Hoot Hoot"

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.food = [self.food[2]]
        self.food_increase_rate = 0.25






class Hen(Bird):
    sound = "Cluck"

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.food_increase_rate = 0.35

