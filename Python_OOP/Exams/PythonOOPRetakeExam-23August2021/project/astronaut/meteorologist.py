from project.astronaut.astronaut import Astronaut

class Meteorologist(Astronaut):

    def __init__(self, name: str):
        super().__init__(name, 90)
        self.default_breath_amount = 15

    def breathe(self):
        self.oxygen -= self.default_breath_amount
