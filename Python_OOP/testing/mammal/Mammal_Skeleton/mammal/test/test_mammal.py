from unittest import TestCase
from project.mammal import Mammal

class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Moockey","monkey","monk-monk")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Moockey")
        self.assertEqual(self.mammal.type, "monkey")
        self.assertEqual(self.mammal.sound, "monk-monk")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(),"Moockey makes monk-monk")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(),"Moockey is of type monkey")
