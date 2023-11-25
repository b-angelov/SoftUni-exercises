from unittest import TestCase
from project.tennis_player import TennisPlayer

class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer(
            "Grishor",
            51,
            3

        )
        self.other_player= TennisPlayer(
            "Jovack Nockovitz",
            62,
            4
        )

    def test_initialization(self):
        player = self.player
        self.assertEqual(player.name, "Grishor")
        self.assertEqual(player.age, 51)
        self.assertEqual(player.points, 3)
        self.assertEqual(player.wins, [])

    def test_name(self):
        player = self.player
        self.assertEqual(player.name,player._TennisPlayer__name)
        with self.assertRaises(ValueError) as ve:
            player.name = "Mo"
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")
        self.assertNotEqual(player.name, "Mo")

    def test_age(self):
        player = self.player
        self.assertEqual(player.age, player._TennisPlayer__age)
        with self.assertRaises(ValueError) as ve:
            player. age = 17
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")
        player.age = 18
        self.assertEqual(player.age, 18)

    def test_add_new_win(self):
        player = self.player
        self.assertEqual(player.add_new_win("Nowhere"), None)
        self.assertEqual(player.wins, ["Nowhere"])
        self.assertEqual(player.add_new_win("Nowhere"), f"Nowhere has been already added to the list of wins!")

    def test_less_than(self):
        player,other = self.player,self.other_player
        self.assertEqual(player < other, f'{other.name} is a top seeded player and he/she is better than {player.name}')
        self.assertEqual(other < player, f'{other.name} is a better player than {player.name}')
        other.points = player.points
        self.assertEqual(other < player, f'{other.name} is a better player than {player.name}')

    def test_str(self):
        self.assertEqual(str(self.player),
                         """Tennis Player: Grishor
Age: 51
Points: 3.0
Tournaments won: """)
        self.player.add_new_win("Nowhere")
        self.player.add_new_win("Everywhere")
        self.assertEqual(str(self.player),
                         """Tennis Player: Grishor
Age: 51
Points: 3.0
Tournaments won: Nowhere, Everywhere""")
