from project.astronaut.astronaut import Astronaut

class Biologist(Astronaut):

    def __init__(self, name: str):
        super().__init__(name, 70)
        self.default_breath_amount = 5

    def breathe(self):
        self.oxygen -= self.default_breath_amount
