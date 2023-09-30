import unittest

# from test_worker import Worker

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Peter", 25.2, 84)

    def test_init(self):
        self.assertEqual(self.worker.name,"Peter")
        self.assertEqual(self.worker.salary,25.2)
        self.assertEqual(self.worker.energy,84)
        self.assertEqual(self.worker.money,0)

    def test_work(self):
        with self.assertRaises(Exception) as msg:
            self.worker.energy = 0
            self.worker.work()
        self.assertEqual(str(msg.exception), 'Not enough energy.')
        self.worker.energy = 84
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)
        self.assertEqual(self.worker.energy, 83)

    def test_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 85)

    def test_get_info(self):
        self.worker.work()
        self.assertEqual(self.worker.get_info(), 'Peter has saved 25.2 money.')

if __name__ == "__main__":
    unittest.main()
