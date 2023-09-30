from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.appliances.laptop import Laptop

class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(),TV(),Fridge(),Fridge(),Laptop(),Laptop()]
        self.calculate_expenses(self.appliances)