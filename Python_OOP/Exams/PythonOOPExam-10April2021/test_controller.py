from unittest import TestCase
from project.controller import *

class TestController(TestCase):

    def setUp(self) -> None:
        self.controller = Controller()

    def test_init(self):
        self.assertEqual(type(self.controller.decorations_repository),DecorationRepository)
        self.assertEqual(self.controller.aquariums,[])

    def test_add_aquarium(self):
        self.assertEqual(self.controller.add_aquarium("AquaSodium","InvalidFishery"),"Invalid aquarium type.")
        self.assertEqual(self.controller.add_aquarium("SaltwaterAquarium","Saltwatery"),f"Successfully added SaltwaterAquarium.")
        self.assertEqual(self.controller.add_aquarium("FreshwaterAquarium","Freshwatery"),f"Successfully added FreshwaterAquarium.")

    def test_add_decoration(self):
        self.assertEqual(self.controller.add_decoration("Nonetype"),"Invalid decoration type.")
        self.assertEqual(self.controller.add_decoration("Plant"),"Successfully added Plant.")
        self.assertEqual(self.controller.add_decoration("Ornament"),"Successfully added Ornament.")

    def test_insert_decoration(self):
        self.controller.add_aquarium("SaltwaterAquarium","MyAqualand")
        self.controller.add_decoration("Plant")
        self.assertEqual(self.controller.insert_decoration("MyAqualand","Ornament"),"There isn't a decoration of type Ornament.")
        self.assertEqual(self.controller.insert_decoration("MyAqualand","Unknown"),"There isn't a decoration of type Unknown.")
        self.controller.add_decoration("Ornament")
        self.assertEqual(self.controller.insert_decoration("MyAqualand","Plant"),f"Successfully added Plant to MyAqualand.")
        self.assertEqual(self.controller.insert_decoration("MyAqualand","Ornament"),f"Successfully added Ornament to MyAqualand.")
        self.assertEqual(self.controller.insert_decoration("MyAqualand","Ornament"),f"There isn't a decoration of type Ornament.")
        self.assertEqual(self.controller.insert_decoration("MyAqualand","Plant"),f"There isn't a decoration of type Plant.")

    def test_add_fish(self):
        self.controller.add_aquarium("SaltwaterAquarium", "MyAqualand")
        self.controller.add_decoration("Plant")
        self.assertEqual(self.controller.add_fish("MyAqualand","MudwaterFish","Albatross","Flying fish",851),"There isn't a fish of type MudwaterFish.")
        self.assertEqual(self.controller.add_fish("MyAqualand","FreshwaterFish","Albatross","Flying fish",851),"Water not suitable." )
        self.assertEqual(self.controller.add_fish("MyAqualand","SaltwaterFish","Albatross","Flying fish",851),"Successfully added SaltwaterFish to MyAqualand." )
        for _ in range(24):
            self.assertEqual(self.controller.add_fish("MyAqualand","SaltwaterFish","Albatross","Flying fish",851),"Successfully added SaltwaterFish to MyAqualand." )
        self.assertEqual(self.controller.add_fish("MyAqualand","SaltwaterFish","Albatross","Flying fish",851),"Not enough capacity.")
        self.controller.add_aquarium("FreshwaterAquarium", "MyAqualandFresh")
        for _ in range(50):
            self.assertEqual(self.controller.add_fish("MyAqualandFresh","FreshwaterFish","Albatross","Flying fish",851),"Successfully added FreshwaterFish to MyAqualandFresh." )
        self.assertEqual(self.controller.add_fish("MyAqualandFresh","FreshwaterFish","Albatross","Flying fish",851),"Not enough capacity.")


    def test_feed_fish(self):
        self.controller.add_aquarium("SaltwaterAquarium", "MyAqualand")
        self.controller.add_decoration("Plant")
        self.assertEqual(self.controller.add_fish("MyAqualand", "MudwaterFish", "Albatross", "Flying fish", 851),"There isn't a fish of type MudwaterFish.")
        self.assertEqual(self.controller.add_fish("MyAqualand", "FreshwaterFish", "Albatross", "Flying fish", 851),"Water not suitable.")
        self.assertEqual(self.controller.add_fish("MyAqualand", "SaltwaterFish", "Albatross", "Flying fish", 851),"Successfully added SaltwaterFish to MyAqualand.")
        self.assertEqual(self.controller.add_fish("MyAqualand", "SaltwaterFish", "Albatross", "Flying fish", 851),"Successfully added SaltwaterFish to MyAqualand.")
        self.assertEqual(self.controller.feed_fish("MyAqualand"),"Fish fed: 2")

    def test_calculate_value(self):
        self.controller.add_aquarium("SaltwaterAquarium", "MyAqualand")
        self.controller.add_decoration("Plant")
        self.assertEqual(self.controller.insert_decoration("MyAqualand", "Ornament"),"There isn't a decoration of type Ornament.")
        self.assertEqual(self.controller.insert_decoration("MyAqualand", "Unknown"),"There isn't a decoration of type Unknown.")
        self.controller.add_decoration("Ornament")
        self.assertEqual(self.controller.insert_decoration("MyAqualand", "Plant"),f"Successfully added Plant to MyAqualand.")
        self.assertEqual(self.controller.insert_decoration("MyAqualand", "Ornament"),f"Successfully added Ornament to MyAqualand.")
        for _ in range(24):
            self.assertEqual(self.controller.add_fish("MyAqualand","SaltwaterFish","Albatross","Flying fish",851.11),"Successfully added SaltwaterFish to MyAqualand." )
        self.assertEqual(self.controller.calculate_value("MyAqualand"), "The value of Aquarium MyAqualand is 20441.64.")

    def test_report(self):
        self.controller.add_aquarium("SaltwaterAquarium", "MyAqualand")
        self.controller.add_decoration("Plant")
        self.controller.insert_decoration("MyAqualand","Plant")
        self.assertEqual(self.controller.add_fish("MyAqualand", "MudwaterFish", "Albatross", "Flying fish", 851),"There isn't a fish of type MudwaterFish.")
        self.assertEqual(self.controller.add_fish("MyAqualand", "FreshwaterFish", "Albatross", "Flying fish", 851),"Water not suitable.")
        self.assertEqual(self.controller.add_fish("MyAqualand", "SaltwaterFish", "Albatross", "Flying fish", 851),"Successfully added SaltwaterFish to MyAqualand.")
        for _ in range(1):
            self.assertEqual(self.controller.add_fish("MyAqualand", "SaltwaterFish", "Albatross", "Flying fish", 851),"Successfully added SaltwaterFish to MyAqualand.")
        self.controller.add_aquarium("FreshwaterAquarium", "MyAqualandFresh")
        for _ in range(1):
            self.assertEqual(self.controller.add_fish("MyAqualandFresh", "FreshwaterFish", "Albatross", "Flying fish", 851),"Successfully added FreshwaterFish to MyAqualandFresh.")
        self.assertEqual(self.controller.report(), """MyAqualand:\nFish: Albatross Albatross\nDecorations: 1\nComfort: 5\nMyAqualandFresh:\nFish: Albatross\nDecorations: 0\nComfort: 0""")
