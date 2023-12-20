from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot("Mountain","Head", 100, 1000)

    def test_initialization(self):
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Mountain', 'Alpine', 'Indoor', 'Bouldering'])
        self.assertEqual(self.robot.category, "Mountain")
        self.assertEqual(self.robot.part_type, "Head")
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 1000)
        self.assertEqual(self.robot.installed_software, [])

    def test_category(self):
        self.robot.category = "Alpine"
        self.assertEqual(self.robot.category, "Alpine")
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "River"
        self.assertEqual(str(ve.exception), f"Category should be one of {self.robot.ALLOWED_CATEGORIES}")
        self.assertEqual(self.robot.category, "Alpine")

    def test_get_used_capacity(self):
        self.assertEqual(self.robot.get_used_capacity(), 0)
        self.robot.install_software({"name":"Monosoft", "capacity_consumption":15,"memory_consumption": 25})
        self.assertEqual(self.robot.get_used_capacity(), 15)

    def test_get_available_capacity(self):
        self.assertEqual(self.robot.get_available_capacity(), 100)
        self.robot.install_software({"name":"Monosoft", "capacity_consumption":15,"memory_consumption": 25})
        self.assertEqual(self.robot.get_available_capacity(), 85)


    def test_get_used_memory(self):
        self.assertEqual(self.robot.get_used_memory(),0)
        self.robot.install_software({"name":"Monosoft", "capacity_consumption":15,"memory_consumption": 25})
        self.assertEqual(self.robot.get_used_memory(),25)

    def test_get_available_memory(self):
        self.assertEqual(self.robot.get_available_memory(), 1000)
        self.robot.install_software({"name":"Monosoft", "capacity_consumption":15,"memory_consumption": 25})
        self.assertEqual(self.robot.get_available_memory(), 975)

    def test_install_software(self):
        self.assertEqual(self.robot.installed_software, [])
        self.assertEqual(self.robot.install_software({"name": "Monosoft", "capacity_consumption": 15, "memory_consumption": 25}), f"Software 'Monosoft' successfully installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [{"name": "Monosoft", "capacity_consumption": 15, "memory_consumption": 25}])
        self.robot.installed_software.clear()
        self.assertEqual(self.robot.install_software({"name": "Monosoft", "capacity_consumption": 100, "memory_consumption": 1000}), f"Software 'Monosoft' successfully installed on Mountain part.")
        self.assertEqual(self.robot.installed_software,[{"name": "Monosoft", "capacity_consumption": 100, "memory_consumption": 1000}])
        self.robot.installed_software.clear()
        self.assertEqual(self.robot.install_software({"name": "Monosoft", "capacity_consumption": 15, "memory_consumption": 25}), f"Software 'Monosoft' successfully installed on Mountain part.")
        self.assertEqual(self.robot.install_software({"name": "Macrosoft", "capacity_consumption": 90, "memory_consumption": 25}), "Software 'Macrosoft' cannot be installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [{"name": "Monosoft", "capacity_consumption": 15, "memory_consumption": 25}])
        self.assertEqual(self.robot.install_software({"name": "Macrosoft", "capacity_consumption": 5, "memory_consumption": 990}), "Software 'Macrosoft' cannot be installed on Mountain part.")
        self.assertEqual(self.robot.installed_software, [{"name": "Monosoft", "capacity_consumption": 15, "memory_consumption": 25}])



if __name__ == '__main__':
    main()
