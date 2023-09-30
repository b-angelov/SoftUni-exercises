import unittest
# from testing.vehicle.Vehicle_Skeleton.vehicle.project.vehicle import Vehicle
from project.vehicle import Vehicle

class VehicleTests(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(51, 182)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 51)
        self.assertEqual(self.vehicle.horse_power, 182)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.capacity, 51)

    def test_drive(self):
        with self.assertRaises(Exception) as msg:
            self.vehicle.drive(182)
        self.assertEqual(str(msg.exception), "Not enough fuel")
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 38.5)

    def test_refuel(self):
        with self.assertRaises(Exception) as msg:
            self.vehicle.refuel(1)
        self.assertEqual(str(msg.exception), "Too much fuel")
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 43.5)

    def test_str(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(str(self.vehicle),
                         """The vehicle has 182 horse power with 43.5 fuel left and 1.25 fuel consumption""")


if __name__ == "__main__":
    unittest.main()
