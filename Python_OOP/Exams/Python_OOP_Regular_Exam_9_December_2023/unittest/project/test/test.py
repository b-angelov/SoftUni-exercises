from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("OutOfRails")

    def test_initialization(self):
        self.assertEqual(self.station._RailwayStation__name, "OutOfRails")
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())

    def test_name(self):
        self.assertEqual(self.station.name, "OutOfRails")
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Out"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Ou"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.assertEqual(self.station.arrival_trains, deque())
        self.station.new_arrival_on_board("Trainless Trainers")
        self.assertEqual(self.station.arrival_trains, deque(['Trainless Trainers']))

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Trainless Trainers")
        self.station.new_arrival_on_board("Trained as Train")
        self.assertEqual(self.station.train_has_arrived("Trained as Train"), "There are other trains to arrive before Trained as Train.")
        self.assertEqual(self.station.arrival_trains, deque(['Trainless Trainers',"Trained as Train"]))
        self.assertEqual(self.station.departure_trains, deque())
        self.assertEqual(self.station.train_has_arrived("Trainless Trainers"), "Trainless Trainers is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.departure_trains, deque(["Trainless Trainers"]))
        self.assertEqual(self.station.arrival_trains, deque(["Trained as Train"]))

    def test_train_has_left(self):
        self.assertFalse(self.station.train_has_left("Trainless train"))
        self.station.new_arrival_on_board("Trainless Train")
        self.station.new_arrival_on_board("Trained as Train")
        self.station.train_has_arrived("Trainless Train")
        self.station.train_has_arrived("Trained as Train")
        self.assertFalse(self.station.train_has_left("Trained as Train"))
        self.assertTrue(self.station.train_has_left("Trainless Train"))



if __name__ == "__main__":
    main()
