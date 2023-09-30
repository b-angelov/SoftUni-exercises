from unittest import TestCase
from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.train = Train(''.join(fc[0] for fc in "The Great Fast Train".split()), 300)

    def test_class_attributes(self):
        self.assertEqual(self.train.TRAIN_FULL, "Train is full")
        self.assertEqual(self.train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(self.train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(self.train.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(self.train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(self.train.ZERO_CAPACITY, 0)

    def test_init(self):
        self.assertEqual(self.train.name, "TGFT")
        self.assertEqual(self.train.capacity, 300)
        self.assertEqual(self.train.passengers, [])

    def test_add_valid(self):
        self.assertEqual(self.train.add("Pilot"), "Added passenger Pilot")
        self.assertEqual(self.train.passengers, ["Pilot"])
        self.assertEqual(self.train.add("Second Pilot"), "Added passenger Second Pilot")
        self.assertEqual(self.train.passengers, ["Pilot","Second Pilot"])

    def test_add_invalid(self):
        self.train.capacity = 1
        self.train.add("Pilot")
        with self.assertRaises(Exception) as msg:
            self.train.add("Second Pilot")
        self.assertEqual(str(msg.exception), "Train is full")
        self.train.capacity = 3
        with self.assertRaises(Exception) as msg:
            self.train.add("Pilot")
        self.assertEqual(str(msg.exception), "Passenger Pilot Exists")
        self.assertEqual(self.train.passengers, ["Pilot"])

    def test_remove_valid(self):
        self.train.add("Pilot")
        self.train.add("Second Pilot")
        self.assertEqual(self.train.remove("Pilot"), "Removed Pilot")
        self.assertEqual(self.train.passengers, ["Second Pilot"])

    def test_remove_invalid(self):
        self.train.add("Pilot")
        self.train.add("Second Pilot")
        with self.assertRaises(Exception) as msg:
            self.train.remove("First Passenger Ever")
        self.assertEqual(str(msg.exception), "Passenger Not Found")
