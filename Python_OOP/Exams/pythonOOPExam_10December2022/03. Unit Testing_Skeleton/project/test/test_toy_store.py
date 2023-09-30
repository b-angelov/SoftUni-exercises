from unittest import TestCase
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_init(self):
        self.assertEqual(self.store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_valid(self):
        self.assertEqual(self.store.add_toy("A","ToyBoy"),f"Toy:ToyBoy placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "ToyBoy")

    def test_add_toy_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.store.add_toy("X","d")
        self.assertEqual(str(msg.exception),"Shelf doesn't exist!")
        self.store.add_toy("A","PuhBear")
        with self.assertRaises(Exception) as msg:
            self.store.add_toy("A","PuhBear")
        self.assertEqual(str(msg.exception), "Toy is already in shelf!")
        with self.assertRaises(Exception) as msg:
            self.store.add_toy("A","BabyRu")
        self.assertEqual(str(msg.exception), "Shelf is already taken!")

    def test_remove_toy_valid(self):
        self.store.add_toy("A","PuhBear")
        self.assertEqual(self.store.remove_toy("A","PuhBear"), f"Remove toy:PuhBear successfully!")
        self.assertEqual(self.store.toy_shelf["A"],None)

    def test_remove_toy_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.store.remove_toy("H","PuhBear")
        self.assertEqual(str(msg.exception), "Shelf doesn't exist!")
        self.store.add_toy("B","GellyBear")
        with self.assertRaises(Exception) as msg:
            self.store.remove_toy("B","PuhBear")
        self.assertEqual(str(msg.exception),"Toy in that shelf doesn't exists!")

