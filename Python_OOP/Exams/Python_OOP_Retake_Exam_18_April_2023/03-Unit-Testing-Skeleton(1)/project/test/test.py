from unittest import TestCase

from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot(
            "AX01Y",
            "Education",
            22,
            814111.22
        )
        self.other_robot = Robot(
            "EOEOA",
            "Entertainment",
            55,
            1521.011
        )

    def test_initialization(self):
        robot = self.robot
        self.assertEqual(robot.robot_id, "AX01Y")
        self.assertEqual(robot.category, "Education")
        self.assertEqual(robot.available_capacity, 22)
        self.assertEqual(robot.price, 814111.22)
        self.assertEqual(robot.hardware_upgrades, [])
        self.assertEqual(robot.software_updates, [])
        self.assertEqual(robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(robot.PRICE_INCREMENT, 1.5)

    def test_category_set(self):
        robot = self.robot
        self.assertEqual(robot.category,robot._Robot__category)
        with self.assertRaises(ValueError) as ve:
            robot.category = "Unique"
        self.assertEqual(str(ve.exception), f"Category should be one of '{robot.ALLOWED_CATEGORIES}'")
        robot.category = "Humanoids"
        self.assertEqual(robot.category, "Humanoids")

    def test_price(self):
        robot = self.robot
        self.assertEqual(robot.price, robot._Robot__price)
        with self.assertRaises(ValueError) as ve:
            robot.price = -1
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade(self):
        robot = self.robot
        self.assertEqual(robot.upgrade("Robomizer", 1000000),f'Robot {robot.robot_id} was upgraded with Robomizer.')
        self.assertEqual(robot.hardware_upgrades,["Robomizer"])
        self.assertEqual(robot.price, 814111.22 + 1000000 * 1.5)
        self.assertEqual(robot.upgrade("Robomizer", 7), f"Robot {robot.robot_id} was not upgraded.")

    def test_update(self):
        robot = self.robot
        self.assertEqual(robot.update(1,21), f'Robot {robot.robot_id} was updated to version 1.')
        self.assertEqual(robot.software_updates,[1])
        self.assertEqual(robot.available_capacity, 1)
        self.assertEqual(robot.update(1, 1), f"Robot {robot.robot_id} was not updated.")
        self.assertEqual(robot.update(1.1,2), f"Robot {robot.robot_id} was not updated.")
        self.assertEqual(robot.software_updates, [1])
        self.assertEqual(robot.available_capacity, 1)

    def test_geater_dan(self):
        robot,other = self.robot,self.other_robot
        self.assertEqual(robot > other, f'Robot with ID {robot.robot_id} is more expensive than Robot with ID {other.robot_id}.')
        other.price = robot.price
        self.assertEqual(robot > other, f'Robot with ID {robot.robot_id} costs equal to Robot with ID {other.robot_id}.')
        other.price += 1
        self.assertEqual(robot > other, f'Robot with ID {robot.robot_id} is cheaper than Robot with ID {other.robot_id}.')