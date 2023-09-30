from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):

    def __init__(self, name: str, price: float):
        self.portion = 250
        self.name = name
        self.price = price

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
