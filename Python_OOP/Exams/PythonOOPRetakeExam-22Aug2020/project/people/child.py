from abc import ABC


class Child(ABC):

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)