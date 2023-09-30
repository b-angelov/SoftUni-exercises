from unittest import TestCase

from project.plantation import Plantation


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(150)

    def test_init(self):
        self.assertEqual(self.plantation.size,150)
        self.assertEqual(self.plantation.plants,{})
        self.assertEqual(self.plantation.workers,[])

    def test_size_valid(self):
        self.plantation.size += 10
        self.assertEqual(self.plantation.size, 160)

    def test_size_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.plantation.size = -1
        self.assertEqual(str(msg.exception), "Size must be positive number!")
        self.assertEqual(self.plantation.size, 150)

    def test_hire_worker_valid(self):
        self.assertEqual(self.plantation.hire_worker("Someone"),f"Someone successfully hired.")
        self.assertIn("Someone",self.plantation.workers)

    def test_hire_worker_invalid(self):
        self.plantation.hire_worker("Someone")
        with self.assertRaises(Exception) as msg:
            self.plantation.hire_worker("Someone")
        self.assertEqual(str(msg.exception), "Worker already hired!")


    def test_planting_valid(self):
        self.plantation.hire_worker("Someone")
        self.assertEqual(self.plantation.planting("Someone","Sunflower"), f"Someone planted it's first Sunflower.")
        self.assertEqual(self.plantation.planting("Someone","Beans"), "Someone planted Beans.")
        self.assertEqual(self.plantation.plants, {"Someone":["Sunflower","Beans"]})

    def test_planting_invalid(self):
        with self.assertRaises(Exception) as msg:
            self.plantation.planting("Anyone","Flowers")
        self.assertEqual(str(msg.exception), "Worker with name Anyone is not hired!")
        self.plantation.hire_worker("Anyone")
        self.plantation.size = 1
        self.plantation.planting("Anyone","Seeds")
        with self.assertRaises(Exception) as msg:
            self.plantation.planting("Anyone", "Roses")
        self.assertEqual(str(msg.exception), "The plantation is full!")

    def test_str(self):
        self.plantation.hire_worker("Someone")
        self.plantation.hire_worker("Anyone")
        self.plantation.planting("Anyone", "Flowers")
        self.plantation.planting("Someone", "Seeds")
        self.plantation.planting("Anyone", "Roses")
        self.assertEqual(str(self.plantation), """Plantation size: 150
Someone, Anyone
Anyone planted: Flowers, Roses
Someone planted: Seeds""")

    def test_repr(self):
        self.plantation.hire_worker("Someone")
        self.plantation.hire_worker("Anyone")
        self.plantation.planting("Anyone", "Flowers")
        self.plantation.planting("Someone", "Seeds")
        self.plantation.planting("Anyone", "Roses")
        self.assertEqual(repr(self.plantation),"""Size: 150
Workers: Someone, Anyone""")

    def test_len(self):
        self.plantation.hire_worker("Someone")
        self.plantation.hire_worker("Anyone")
        self.plantation.planting("Anyone", "Flowers")
        self.plantation.planting("Someone", "Seeds")
        self.plantation.planting("Anyone", "Roses")
        self.assertEqual(len(self.plantation), 3)