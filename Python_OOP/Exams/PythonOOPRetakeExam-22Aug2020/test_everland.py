from unittest import TestCase
from project.everland import Everland
from project.rooms.young_couple import YoungCouple
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.rooms.alone_young import AloneYoung
from project.rooms.alone_old import AloneOld
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.people.child import Child


class TestEverland(TestCase):

    def setUp(self) -> None:
        self.hotel = Everland()
        self.young_couple = YoungCouple("младодвойкови",10,20)
        self.young_couple_with_children = YoungCoupleWithChildren("младодечкови",10,30,Child(1,5,1,1),Child(2,11,2,1))
        self.old_couple = OldCouple("стародвойкови",5,10)
        self.alone_young = AloneYoung("момък",25)
        self.alone_old = AloneOld("старец",15)


    def test_init(self):
        self.assertEqual(self.hotel.rooms,[])
        self.assertEqual([type(appliance) for appliance in self.young_couple.appliances], [TV, TV, Fridge, Fridge, Laptop, Laptop])
        self.assertEqual(self.young_couple.room_cost, 20)
        self.assertEqual(self.young_couple.expenses, 7.4 * 30)
        self.assertEqual([type(appliance) for appliance in self.old_couple.appliances], [TV, TV, Fridge, Fridge, Stove, Stove])
        self.assertEqual(self.old_couple.room_cost, 15)
        self.assertEqual(self.old_couple.expenses, 6.8 * 30)
        self.assertEqual([type(appliance) for appliance in self.young_couple_with_children.appliances], [TV, TV, TV, TV, Fridge, Fridge, Fridge, Fridge, Laptop, Laptop, Laptop, Laptop])
        self.assertEqual(self.young_couple_with_children.room_cost, 30)
        self.assertEqual(self.young_couple_with_children.expenses, 14.8 * 30 + 24 * 30)
        self.assertEqual([type(appliance) for appliance in self.alone_young.appliances], [TV])
        self.assertEqual(self.alone_young.room_cost, 10)
        self.assertEqual(self.alone_young.expenses, 1.5*30)
        self.assertEqual([type(appliance) for appliance in self.alone_old.appliances], [])
        self.assertEqual(self.alone_old.room_cost, 10)
        self.assertEqual(self.alone_old.expenses, 0)


    def test_add_room(self):
        self.assertEqual(self.hotel.add_room(self.young_couple),None)
        self.assertEqual(self.hotel.rooms,[self.young_couple])

    def test_get_monthly_consumptions(self):
        self.hotel.add_room(self.young_couple)
        self.hotel.add_room(self.old_couple)
        self.hotel.add_room(self.young_couple_with_children)
        self.assertEqual(self.hotel.get_monthly_consumptions(),f"Monthly consumption: {(20 + 7.4*30) + (15+6.8*30) + (30 + (14.8 * 30 + 24 * 30)):.2f}$.")

    def test_pay(self):
        self.hotel.add_room(self.young_couple)
        self.young_couple.budget = 5000
        self.hotel.add_room(self.old_couple)
        self.hotel.add_room(self.young_couple_with_children)
        self.assertEqual(self.hotel.pay(),"""младодвойкови paid 242.00$ and have 4758.00$ left.
стародвойкови does not have enough budget and must leave the hotel.
младодечкови does not have enough budget and must leave the hotel.""")

    def test_status(self):
        self.hotel.add_room(self.young_couple)
        self.young_couple.budget = 5000
        self.hotel.add_room(self.old_couple)
        self.hotel.add_room(self.young_couple_with_children)
        self.hotel.pay()
        self.assertEqual(self.hotel.status(),"""Total population: 8
младодвойкови with 2 members. Budget: 5000.00$, Expenses: 222.00$
--- Appliances monthly cost: 222.00$
стародвойкови with 2 members. Budget: 15.00$, Expenses: 204.00$
--- Appliances monthly cost: 204.00$
младодечкови with 4 members. Budget: 40.00$, Expenses: 1164.00$
--- Child 1 monthly cost: 240.00$
--- Child 2 monthly cost: 480.00$
--- Appliances monthly cost: 444.00$""")
