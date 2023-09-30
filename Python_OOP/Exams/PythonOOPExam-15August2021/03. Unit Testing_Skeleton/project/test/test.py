from unittest import TestCase

from project.pet_shop import PetShop


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.shop = PetShop("Pettery")

    def test_init(self):
        self.assertEqual(self.shop.name, "Pettery")
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_add_food_valid(self):
        self.assertEqual(self.shop.add_food("Kitten's food", 1000),f"Successfully added 1000.00 grams of Kitten's food.")
        self.assertEqual(self.shop.add_food("Kitten's food", 10),f"Successfully added 10.00 grams of Kitten's food.")
        self.assertEqual(self.shop.food, {"Kitten's food":1010})

    def test_add_food_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.shop.add_food("Puppy's food", 0)
        self.assertEqual(str(msg.exception), 'Quantity cannot be equal to or less than 0')
        with self.assertRaises(Exception) as msg:
            self.shop.add_food("Puppy's food", -1)
        self.assertEqual(str(msg.exception), 'Quantity cannot be equal to or less than 0')
        self.assertEqual(self.shop.food, {})

    def test_add_pet_valid(self):
        self.assertEqual(self.shop.add_pet("Puppy"), f"Successfully added Puppy.")
        self.assertEqual(self.shop.add_pet("Kitty"), f"Successfully added Kitty.")
        self.assertEqual(self.shop.pets, ["Puppy", "Kitty"])

    def test_add_pet_invalid(self):
        self.shop.add_pet("Puppy")
        with self.assertRaises(Exception) as msg:
            self.shop.add_pet("Puppy")
        self.assertEqual(str(msg.exception), "Cannot add a pet with the same name")
        self.assertEqual(self.shop.pets, ["Puppy"])

    def test_feed_pet_valid(self):
        self.shop.add_pet("Kitty")
        self.shop.add_pet("Puppy")
        self.shop.add_food("Kitty's food", 1)
        self.assertEqual(self.shop.feed_pet("Kitty's food", "Kitty"), f"Adding food...")
        self.assertEqual(self.shop.food["Kitty's food"], 1001)
        self.assertEqual(self.shop.feed_pet("Kitty's food", "Kitty"), f"Kitty was successfully fed")
        self.assertEqual(self.shop.food["Kitty's food"], 901)
        self.assertEqual(self.shop.pets, ["Kitty","Puppy"])



    def test_feed_pet_invalid(self):
        self.shop.add_pet("Somepy")
        with self.assertRaises(Exception) as msg:
            self.shop.feed_pet("Nonepy's food","Nonepy")
        self.assertEqual(str(msg.exception), "Please insert a valid pet name")
        self.assertEqual(self.shop.feed_pet("Somepy's food", "Somepy"), 'You do not have Somepy\'s food')

    def test_repr(self):
        self.shop.add_pet("Kitty")
        self.shop.add_pet("Puppy")
        self.shop.add_food("Puppy's food", 1)
        self.shop.add_food("Kitty's food", 10)
        self.assertEqual(repr(self.shop), """Shop Pettery:
Pets: Kitty, Puppy""")
