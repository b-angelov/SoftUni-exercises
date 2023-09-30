import unittest
# from testing.hero.Hero_Skeleton.hero.project.hero import Hero
from project.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Heracules",184,101,1847)
        self.enemy_hero = Hero("Enemaleous",111,351,1254)

    def test_init(self):
        self.assertEqual(self.hero.username, "Heracules")
        self.assertEqual(self.hero.level, 184)
        self.assertEqual(self.hero.health, 101)
        self.assertEqual(self.hero.damage, 1847)

    def test_battle(self):
        with self.assertRaises(Exception) as msg:
            self.hero.battle(self.hero)
        self.assertEqual(str(msg.exception), "You cannot fight yourself")
        self.hero.health = 0
        with self.assertRaises(Exception) as msg:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), "Your health is lower than or equal to 0. You need to rest")
        self.hero.health = 101
        self.enemy_hero.health = 0
        with self.assertRaises(Exception) as msg:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), "You cannot fight Enemaleous. He needs to rest")
        self.hero.health = 1_000_000
        self.enemy_hero.health = 1_000_000
        self.assertEqual(self.hero.battle(self.enemy_hero),"You lose")
        self.assertEqual(self.hero.health,860806)
        self.assertEqual(self.enemy_hero.health,660157)
        self.assertEqual(self.enemy_hero.level,112)
        self.assertEqual(self.enemy_hero.damage,1259)
        self.hero.health = 1_000_000
        self.enemy_hero.health = 5000
        self.assertEqual(self.hero.battle(self.enemy_hero), "You win")
        self.assertEqual(self.hero.health, 858997)
        self.assertEqual(self.enemy_hero.health, -334848)
        self.hero.health = 1
        self.enemy_hero.health = 2
        self.assertEqual(self.hero.battle(self.enemy_hero), "Draw")

    def test_str(self):
        self.assertEqual(str(self.hero), """Hero Heracules: 184 lvl
Health: 101
Damage: 1847
""")

if __name__ == "__main__":
    unittest.main()
