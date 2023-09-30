from project.horse_specification.horse import Horse
# from horse import Horse

class Appaloosa(Horse):

    def __init__(self, name: str, speed: int):
        self.horse_max_speed = 120
        self._speed = None
        super().__init__(name,speed)
        self.add = 2

    def train(self):
        self.speed += self.add
