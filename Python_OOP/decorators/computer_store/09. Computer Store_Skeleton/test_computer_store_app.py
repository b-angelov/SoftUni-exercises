from unittest import TestCase
from project.computer_store_app import ComputerStoreApp, Laptop


class TestComputerStoreApp(TestCase):

    def setUp(self) -> None:
        self.store = ComputerStoreApp()

    def test_build_computer(self):
        with self.assertRaises(ValueError) as msg:
            self.store.build_computer("Mesklop", 1, 1, 1 ,1)
        self.assertEqual(str(msg.exception), f"Mesklop is not a valid type computer!")
        with self.assertRaises(ValueError) as msg:
            self.store.build_computer("Laptop", "    ", 1, 1 ,1)
        self.assertEqual(str(msg.exception), "Manufacturer name cannot be empty.")
        with self.assertRaises(ValueError) as msg:
            self.store.build_computer("Laptop", "ropenshield ltd.", "   ", 1 ,1)
        self.assertEqual(str(msg.exception), "Model name cannot be empty.")
        with self.assertRaises(ValueError) as msg:
            self.store.build_computer("Laptop", "ropenshield ltd.", "Loposchwieb 10" , "Shieldproc 11",1)
        self.assertEqual(str(msg.exception), "Shieldproc 11 is not compatible with laptop ropenshield ltd. Loposchwieb 10!")
        with self.assertRaises(ValueError) as msg:
            self.store.build_computer("Desktop Computer", "ropenshield ltd.", "Loposchwieb 10" , "Shieldproc 11",1)
        self.assertEqual(str(msg.exception), "Shieldproc 11 is not compatible with desktop computer ropenshield ltd. Loposchwieb 10!")
        n = Laptop._power_of_two(150)
        powers_of_two = list(2 ** i for i in range(1,8))
        for i in range(0, 150):
            if i not in powers_of_two:
                with self.assertRaises(ValueError) as msg:
                    self.store.build_computer("Desktop Computer", "ropenshield ltd.", "Loposchwieb 10" , "Intel Core i5-12600K",i)
                self.assertEqual(str(msg.exception), f"{i}GB RAM is not compatible with desktop computer ropenshield ltd. Loposchwieb 10!")

    def test_sell_computer(self):
        self.fail()
