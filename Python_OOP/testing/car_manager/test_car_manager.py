import unittest
from testing.car_manager.CarManager.car_manager import Car


class CarTests(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("some", "chavdar", 11, 151)

    def test_init(self):
        self.assertEqual(self.car.make, "some")
        self.assertEqual(self.car.model, "chavdar")
        self.assertEqual(self.car.fuel_consumption, 11)
        self.assertEqual(self.car.fuel_capacity, 151)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make(self):
        self.assertEqual(self.car.make, "some")
        with self.assertRaises(Exception) as msg:
            self.car.make = ""
        self.assertEqual(str(msg.exception), "Make cannot be null or empty!")

    def test_model(self):
        self.assertEqual(self.car.model, "chavdar")
        with self.assertRaises(Exception) as msg:
            self.car.model = ""
        self.assertEqual(str(msg.exception), "Model cannot be null or empty!")

    def test_fuel_consumption(self):
        self.assertEqual(self.car.fuel_consumption, 11)
        with self.assertRaises(Exception) as msg:
            self.car.fuel_consumption = 0
        self.assertEqual(str(msg.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity(self):
        self.assertEqual(self.car.fuel_capacity, 151)
        with self.assertRaises(Exception) as msg:
            self.car.fuel_capacity = 0
        self.assertEqual(str(msg.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount(self):
        self.assertEqual(self.car.fuel_amount, 0)
        with self.assertRaises(Exception) as msg:
            self.car.fuel_amount = -1
        self.assertEqual(str(msg.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount,1)
        self.car.fuel_amount = 151
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount,151)
        with self.assertRaises(Exception) as msg:
            self.car.refuel(0)
        self.assertEqual(str(msg.exception), "Fuel amount cannot be zero or negative!")


    def test_drive(self):
        with self.assertRaises(Exception) as msg:
            self.car.drive(5)
        self.assertEqual(str(msg.exception),"You don't have enough fuel to drive!")
        self.car.refuel(60)
        self.car.drive(500)
        self.assertEqual(self.car.fuel_amount, 5)

if __name__ == "__main__":
    unittest.main()
