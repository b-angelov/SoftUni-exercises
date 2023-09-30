import unittest

# from testing.list.List.extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1,4,2,5,7)

    def test_init(self):
        list = IntegerList(1, 4 ,5, "Krusha",8,"Pechka",12, 22, str )
        self.assertEqual(list._IntegerList__data,[1,4,5,8,12,22])


    def test_get_data(self):
        self.assertEqual(self.list.get_data(),[1,4,2,5,7])

    def test_add(self):
        with self.assertRaises(ValueError) as msg:
            self.list.add("str")
        self.assertEqual(str(msg.exception),"Element is not Integer")
        self.assertEqual(self.list.add(9), [1,4,2,5,7,9])
        self.assertEqual(self.list._IntegerList__data,[1,4,2,5,7,9])

    def test_remove_index(self):
        with self.assertRaises(IndexError) as msg:
            self.list.remove_index(5)
        self.assertEqual(str(msg.exception),"Index is out of range")
        self.assertEqual(self.list.remove_index(0), 1)
        self.assertEqual(self.list._IntegerList__data, [4,2,5,7])

    def test_get(self):
        with self.assertRaises(IndexError) as msg:
            self.list.get(5)
        self.assertEqual(str(msg.exception), "Index is out of range")
        self.assertEqual(self.list.get(4),7)

    def test_insert(self):
        with self.assertRaises(IndexError) as msg:
            self.list.insert(9,5)
        self.assertEqual(str(msg.exception), "Index is out of range")
        with self.assertRaises(ValueError) as msg:
            self.list.insert(4,"9")
        self.assertEqual(str(msg.exception), "Element is not Integer")
        self.list.insert(4, 9)
        self.assertEqual(self.list._IntegerList__data,[1,4,2,5,9,7])

    def test_get_biggest(self):
        self.assertEqual(self.list.get_biggest(), 7)

    def test_get_index(self):
        self.assertEqual(self.list.get_index(7),4)

if __name__ == "__main__":
    unittest.main()
