from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("MyRailway")

    def test_initialization(self):
        self.assertEqual(self.station.name, "MyRailway")
        self.assertEqual(self.station._RailwayStation__name, "MyRailway")
        self.assertEqual(type(self.station.arrival_trains), deque)
        self.assertEqual(type(self.station.departure_trains), deque)

    def test_name(self):
        self.assertEqual(self.station.name,"MyRailway")
        with self.assertRaises(ValueError) as ve:
            self.station.name = "rai"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")
        self.assertEqual(self.station.name, "MyRailway")
        with self.assertRaises(ValueError) as ve:
            self.station.name = "ra"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")
        self.assertEqual(self.station.name, "MyRailway")

    def test_new_arrival_on_board(self):
        self.assertEqual(self.station.arrival_trains, deque())
        self.station.new_arrival_on_board("Anyone")
        self.assertEqual(self.station.arrival_trains[-1],"Anyone")

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Anyone")
        self.station.new_arrival_on_board("Someone")
        self.assertEqual(self.station.train_has_arrived("Someone"), "There are other trains to arrive before Someone.")
        self.assertEqual(self.station.arrival_trains, deque(["Anyone","Someone"]))
        self.assertEqual(self.station.train_has_arrived("Anyone"), "Anyone is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.arrival_trains, deque(["Someone"]))
        self.assertEqual(self.station.departure_trains, deque(["Anyone"]))
        self.assertEqual(self.station.arrival_trains, deque(["Someone"]))

    def test_train_has_left(self):
        self.station.new_arrival_on_board("Anyone")
        self.station.train_has_arrived("Anyone")
        self.assertEqual(self.station.train_has_left("Anyone"), True)
        self.assertEqual(self.station.train_has_left("Someone"), False)
        self.station.new_arrival_on_board("Anyone")
        self.station.train_has_arrived("Anyone")
        self.station.new_arrival_on_board("Someone")
        self.station.train_has_arrived("Someone")
        self.assertEqual(self.station.train_has_left("Someone"), False)

if __name__ == '__main__':
    main()
