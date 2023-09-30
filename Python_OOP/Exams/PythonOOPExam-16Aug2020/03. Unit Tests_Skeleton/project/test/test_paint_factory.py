from unittest import TestCase
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.factory = PaintFactory("MyFactory", 200)

    def test_init(self):
        self.assertEqual(self.factory.name, "MyFactory")
        self.assertEqual(self.factory.capacity, 200)
        self.assertEqual(self.factory.ingredients, {})
        self.assertEqual(self.factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_valid(self):
        self.assertEqual(self.factory.add_ingredient("white", 12), None)
        self.assertEqual(self.factory.ingredients,{"white":12})

    def test_add_ingredient_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.factory.add_ingredient("white", 201)
        self.assertEqual(str(msg.exception), "Not enough space in factory")
        with self.assertRaises(TypeError) as msg:
            self.factory.add_ingredient("purple", 201)
        self.assertEqual(str(msg.exception), "Ingredient of type purple not allowed in PaintFactory")


    def test_remove_ingredient_valid(self):
        self.factory.add_ingredient("yellow", 151)
        self.assertEqual(self.factory.remove_ingredient("yellow", 100), None)
        self.assertEqual(self.factory.ingredients, {"yellow":51})

    def test_remove_ingredient_invalid(self):
        self.factory.add_ingredient("yellow", 151)
        with self.assertRaises(ValueError) as msg:
            self.factory.remove_ingredient("yellow",152)
        self.assertEqual(str(msg.exception), "Ingredients quantity cannot be less than zero")
        with self.assertRaises(KeyError) as msg:
            self.factory.remove_ingredient("yellows",156)
        self.assertEqual(str(msg.exception), "'No such ingredient in the factory'")
        self.assertEqual(self.factory.ingredients, {"yellow":151})

    def test_products(self):
        self.factory.add_ingredient("white", 101)
        self.factory.add_ingredient("yellow", 64)
        self.assertEqual(self.factory.products, {"white": 101, "yellow": 64})

    def test_can_add(self):
        self.factory.add_ingredient("white", 101)
        self.factory.add_ingredient("yellow", 64)
        self.assertEqual(self.factory.can_add(10), True)
        self.assertEqual(self.factory.can_add(40), False)

    def test_repr(self):
        self.assertEqual(repr(self.factory), "Factory name: MyFactory with capacity 200.\n")
        self.factory.add_ingredient("white", 101)
        self.factory.add_ingredient("yellow", 64)
        self.assertEqual(repr(self.factory), """Factory name: MyFactory with capacity 200.
white: 101
yellow: 64\n""")
