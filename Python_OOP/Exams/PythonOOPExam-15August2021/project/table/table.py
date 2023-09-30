from abc import ABC, abstractmethod
from project.common_functions import exc
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink

class Table(ABC):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders,self.drink_orders = [],[]
        self.number_of_people = 0
        self.is_reserved = False

    def reserve(self, number_of_people: int):
        self.is_reserved = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(drink.price for drink in self.drink_orders) + sum(food.price for food in self.food_orders)

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return '\n'.join((f"Table: {self.table_number}",f"Type: {self.__class__.__name__}",f"Capacity: {self.capacity}"))



    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        exc("Capacity has to be greater than 0!",capacity <= 0)
        self.__capacity = capacity

    @property
    def is_reserved(self):
        return self.__is_reserved
    @is_reserved.setter
    def is_reserved(self, people):
        self.number_of_people = int(people)
        self.__is_reserved = bool(people)

    @property
    @abstractmethod
    def table_number(self):
        ...
