from unittest import TestCase

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar(
            "BulgarCar Nevermobile",
            "Eine sehr gross wagen",
            989000,
            57.12
        )

    def test_initialization(self):
        car =self.car
        self.assertEqual(car.model, "BulgarCar Nevermobile")
        self.assertEqual(car.car_type, "Eine sehr gross wagen")
        self.assertEqual(car.mileage, 989000)
        self.assertEqual(car.price, 57.12)
        self.assertEqual(car.repairs,[])

    def test_price_set(self):
        car = self.car
        self.assertEqual(car.price, car._price)
        with self.assertRaises(ValueError) as ve:
            car.price = 1.00
        self.assertEqual(str(ve.exception), 'Price should be greater than 1.0!')
        car.price = 1.01
        self.assertEqual(car.price, 1.01)

    def test_mileage_set(self):
        car = self.car
        self.assertEqual(car._mileage, 989000)
        self.assertEqual(car.mileage,car._mileage)
        with self.assertRaises(ValueError) as ve:
            car.mileage = 100
        self.assertEqual(str(ve.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price(self):
        car = self.car
        with self.assertRaises(ValueError) as ve:
            car.set_promotional_price(car.price + 1)
        self.assertEqual(str(ve.exception), 'You are supposed to decrease the price!')
        self.assertEqual(car.set_promotional_price(car.price - 0.12), 'The promotional price has been successfully set.')
        self.assertAlmostEqual(car.price, 57)

    def test_need_repair(self):
        car = self.car
        self.assertEqual(car.need_repair(42, "Тая бръкма няма ли да я даваш за скрап вече?"), 'Repair is impossible!')
        self.assertEqual(car.need_repair(28.56, "Аз трябва да ти дам че ми го разкара това от погледа ама айде дай - 28.56лв. и се махай."),'Price has been increased due to repair charges.')
        self.assertAlmostEqual(car.price, 85.68)
        self.assertEqual(car.repairs,["Аз трябва да ти дам че ми го разкара това от погледа ама айде дай - 28.56лв. и се махай."])

    def test_gt(self):
        car = self.car
        your_car = SecondHandCar("a","b",211,22)
        self.assertEqual((car > your_car), 'Cars cannot be compared. Type mismatch!')
        your_car.car_type = car.car_type
        self.assertTrue(car > your_car)

    def test_str(self):
        self.assertEqual(str(self.car), """Model BulgarCar Nevermobile | Type Eine sehr gross wagen | Milage 989000km
Current price: 57.12 | Number of Repairs: 0""")


