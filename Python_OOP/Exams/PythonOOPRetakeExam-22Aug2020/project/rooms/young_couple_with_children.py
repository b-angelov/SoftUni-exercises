from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.appliances.laptop import Laptop

class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = list(children)
        family_count = 2 + len(children)
        self.appliances = ([TV()] * family_count) + ([Fridge()] * family_count) + ([Laptop()] * family_count)
        self.calculate_expenses(self.appliances,self.children)

