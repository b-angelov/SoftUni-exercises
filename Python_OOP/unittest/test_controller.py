from unittest import TestCase
from project.controller import *
from project.supply.drink import Drink
from project.supply.food import Food
from project.player import Player


class TestController(TestCase):

    def setUp(self) -> None:
        self.controller = Controller()
        # Player.player_list.clear()
        Player.players_names.clear()
        self.player1 = Player("George",20,75)
        self.player2 = Player("Robert",19,88)
        self.player3 = Player("Sir Playson", 65, 41)
        self.drink1 = Drink("water")
        self.drink2 = Drink("Juice")
        self.drink3 = Drink("wine")
        self.food1 = Food("bread", 30)
        self.food2 = Food("apple", 15)
        self.food3 = Food("meat", 20)

    def test_init(self):
        self.assertEqual(self.controller.players, [])
        self.assertEqual(self.controller.supplies, [])

    def test_add_player(self):
        self.assertEqual(self.controller.add_player(self.player1,self.player2), "Successfully added: George, Robert")
        self.assertEqual(self.controller.add_player(self.player1,self.player2,self.player3), "Successfully added: Sir Playson")
        self.assertEqual(self.controller.players, [self.player1,self.player2,self.player3])

    def test_add_supply(self):
        self.assertEqual(self.controller.add_supply(self.drink1,self.drink2,self.drink1,self.food3,self.food1), None)
        self.assertEqual(self.controller.supplies, [self.drink1,self.drink2,self.drink1,self.food3,self.food1])

    def test_sustain_valid(self):
        self.controller.add_player(self.player1, self.player2, self.player3)
        self.controller.add_supply(self.drink1, self.drink2, self.drink1, self.food3, self.food1)
        self.assertEqual(self.controller.sustain(self.player1.name, "Drink"), f"George sustained successfully with {self.drink1.name}.")
        self.assertEqual(self.controller.supplies, [self.drink1, self.drink2,self.food3, self.food1])
        self.assertEqual(self.controller.players[0].stamina, 90)
        self.assertEqual(self.controller.sustain(self.player1.name, "Food"), f"George sustained successfully with {self.food1.name}.")
        self.assertEqual(self.controller.supplies, [self.drink1, self.drink2,self.food3])
        self.assertEqual(self.controller.players[0].stamina, 100)
        self.assertEqual(self.controller.sustain(self.player1.name, "Drink"), "George have enough stamina.")
        self.assertEqual(self.controller.sustain(self.player1.name, "Food"), "George have enough stamina.")
        self.assertEqual(self.controller.players[0].stamina, 100)


    def test_sustain_invalid(self):
        self.controller.add_player(self.player1, self.player2, self.player3)
        self.controller.add_supply(self.drink1, self.drink2, self.drink1)
        with self.assertRaises(Exception) as msg:
            self.assertEqual(self.controller.sustain(self.player1.name, "Food"),f"George sustained successfully with {self.food1.name}.")
        self.assertEqual(str(msg.exception), "There are no food supplies left!")
        self.controller.supplies.clear()
        self.controller.add_supply(self.food3, self.food1)
        with self.assertRaises(Exception) as msg:
            self.assertEqual(self.controller.sustain(self.player1.name, "Drink"),f"George sustained successfully with {self.food1.name}.")
        self.assertEqual(str(msg.exception), "There are no drink supplies left!")
        self.assertEqual(self.controller.sustain("Jane", "Drink"), None)
        self.assertEqual(self.controller.sustain("Robert", "Kiss"), None)

    def test_duel_valid(self):
        self.controller.add_player(self.player1, self.player2, self.player3)
        self.controller.add_supply(self.drink1, self.drink2, self.drink1, self.food3, self.food1)
        self.assertEqual(self.controller.duel("George","Robert"), "Winner: Robert")
        self.assertEqual(self.player1.stamina, 49.75)
        self.assertEqual(self.player2.stamina, 50.50)

    def test_duel_valid2(self):
        self.controller.add_player(self.player1, self.player2, self.player3)
        self.player1.stamina = 80
        self.player2.stamina = 10
        self.controller.add_supply(self.drink1, self.drink2, self.drink1, self.food3, self.food1)
        self.assertEqual(self.controller.duel("George","Robert"), "Winner: George")
        self.assertEqual(self.player1.stamina, 75)
        self.assertEqual(self.player2.stamina, 0)

    def test_duel_invalid(self):
        self.controller.add_player(self.player1, self.player2, self.player3)
        self.player1.stamina = 0
        self.player2.stamina = 10
        self.assertEqual(self.controller.duel("George","Robert"), "Player George does not have enough stamina." )
        self.player1.stamina = 1
        self.player2.stamina = 0
        self.assertEqual(self.controller.duel("George","Robert"), "Player Robert does not have enough stamina." )
        self.player1.stamina = 0
        self.player2.stamina = 0
        self.assertEqual(self.controller.duel("George","Robert"), "Player George does not have enough stamina.\nPlayer Robert does not have enough stamina." )

    def test_next_day(self):
        self.controller.add_player(self.player1, self.player2, self.player3)
        self.controller.add_supply(self.drink1, self.drink2, self.drink2, self.drink1, self.food3, self.food1, self.food1)
        self.player1.stamina = 3
        self.assertEqual(self.controller.next_day(), None)
        self.assertEqual(self.controller.supplies, [self.drink1])
        self.assertEqual(self.player1.stamina, self.drink1.energy + self.food1.energy)
        self.assertEqual(self.player2.stamina,88 - (self.player2.age*2) + self.food1.energy + self.drink2.energy)
        self.assertEqual(self.player3.stamina, 0 + self.drink2.energy + self.food3.energy)#41 - 65*2 + self.drink2.energy + self.food3.energy)


