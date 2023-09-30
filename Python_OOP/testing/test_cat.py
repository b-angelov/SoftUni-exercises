class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

import unittest

class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Rizzhio")
    
    def test_eat(self):
        self.assertEqual(self.cat.size, 0)
        self.assertEqual(self.cat.fed, False)
        self.assertEqual(self.cat.sleepy, False)
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)
        self.assertEqual(self.cat.fed, True)
        self.assertEqual(self.cat.sleepy, True)
        self.assertRaises(Exception,self.cat.eat)

    def test_sleep(self):
        self.assertRaises(Exception,self.cat.sleep)
        self.cat.eat()
        self.assertEqual(self.cat.sleepy, True)
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)

if __name__ == "__main__":
    unittest.main()