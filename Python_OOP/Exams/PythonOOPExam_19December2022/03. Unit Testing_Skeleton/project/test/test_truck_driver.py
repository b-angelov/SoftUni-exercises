from unittest import TestCase

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Me", 212)

    def test_init(self):
        self.assertEqual(self.driver.name, "Me")
        self.assertEqual(self.driver.money_per_mile, 212)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_valid(self):
        self.driver.earned_money = 1
        self.assertEqual(self.driver.earned_money, 1)

    def test_earned_money_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.driver.earned_money = -1
        self.assertEqual(str(msg.exception), f"{self.driver.name} went bankrupt.")

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("Somewhere", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_valid(self):
        self.assertEqual(self.driver.add_cargo_offer("Somewhere", 512),
                         f"Cargo for 512 to Somewhere was added as an offer.")
        self.assertEqual("Somewhere" in self.driver.available_cargos.keys(), True)
        self.assertEqual(self.driver.available_cargos["Somewhere"], 512)

    def test_add_cargo_offer_invalid(self):
        self.driver.add_cargo_offer("Somewhere", 512)
        with self.assertRaises(Exception) as msg:
            self.driver.add_cargo_offer("Somewhere", 512)
        self.assertEqual(str(msg.exception), "Cargo offer is already added.")

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("Somewhere", 512)
        self.driver.add_cargo_offer("Nowhere", 1)
        self.assertEqual(self.driver.drive_best_cargo_offer(), f"{self.driver.name} is driving 512 to Somewhere.")
        self.assertEqual(self.driver.miles, 512)
        self.assertEqual(self.driver.earned_money, 512*212 - 40)

    def test_drive_best_cargo_offer_invalid(self):
        res = self.driver.drive_best_cargo_offer()
        self.assertEqual(res, "There are no offers available.")

    def test_check_for_activities_invalid(self):
        self.assertRaises(Exception, self.driver.check_for_activities, 512)

    def test_check_for_activities_valid(self):
        self.driver.add_cargo_offer("Somewhere", 512)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.check_for_activities(512), None)

    def test_eat_valid(self):
        self.driver.earned_money = 0
        self.assertEqual(self.driver.eat(249), None)
        self.assertEqual(self.driver.eat(251), None)
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.earned_money = 250
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 230)
        self.driver.eat(500)
        self.assertEqual(self.driver.earned_money, 210)

    def test_eat_invalid(self):
        self.assertRaises(Exception, self.driver.eat, 250)

    def test_sleep_valid(self):
        self.driver.earned_money = 0
        self.assertEqual(self.driver.sleep(999), None)
        self.assertEqual(self.driver.sleep(1001), None)
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.earned_money = 250
        self.driver.sleep(1000)
        self.assertEqual(self.driver.earned_money, 205)
        self.driver.sleep(2000)
        self.assertEqual(self.driver.earned_money, 160)

    def test_sleep_invalid(self):
        self.assertRaises(Exception, self.driver.sleep, 1000)

    def test_pump_gas_valid(self):
        self.driver.earned_money = 0
        self.assertEqual(self.driver.pump_gas(1499), None)
        self.assertEqual(self.driver.pump_gas(1501), None)
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(self.driver.earned_money, 500)
        self.driver.pump_gas(3000)
        self.assertEqual(self.driver.earned_money, 0)

    def test_pump_gas_invalid(self):
        self.assertRaises(Exception, self.driver.pump_gas, 1500)

    def test_repair_truck_valid(self):
        self.driver.earned_money = 0
        self.assertEqual(self.driver.repair_truck(9999), None)
        self.assertEqual(self.driver.repair_truck(10001), None)
        self.assertEqual(self.driver.earned_money, 0)
        self.driver.earned_money = 20000
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 12500)
        self.driver.repair_truck(20000)
        self.assertEqual(self.driver.earned_money, 5000)

    def test_repair_truck_invalid(self):
        self.assertRaises(Exception, self.driver.repair_truck, 10000)

    def test_repr(self):
        self.driver.earned_money = 0
        self.assertEqual(str(self.driver), f"Me has 0 miles behind his back.")
        self.driver.add_cargo_offer("Somewhere", 512)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(str(self.driver), f"Me has 512 miles behind his back.")
