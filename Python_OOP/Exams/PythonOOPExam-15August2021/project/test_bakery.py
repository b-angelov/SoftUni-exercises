from unittest import TestCase
from bakery import Bakery
# bakery = Bakery("My bake")

class TestBakery(TestCase):

    def setUp(self):
        self.bakery = Bakery("My bake")

    def test_add_food(self):
        self.assertEqual(self.bakery.add_food("Nothing","None",0), None)
        self.assertEqual(self.bakery.add_food("Cake","None",1), "Added None (Cake) to the food menu")
        with self.assertRaises(Exception) as ms:
            self.bakery.add_food("Cake","None",1)
        self.assertEqual(str(ms.exception), "Cake None is already in the menu!")

    def test_add_drink(self):
        self.assertEqual(self.bakery.add_drink("drinkType", "DrinkNme", 0, "drinkBrand"), None)
        self.assertEqual(self.bakery.add_drink("Water", "drinkName", 1, "Brand"), "Added drinkName (Brand) to the drink menu")
        with self.assertRaises(Exception) as ms:
            self.bakery.add_drink("Water", "drinkName", 1, "Brand")
        self.assertEqual(str(ms.exception), "Water drinkName is already in the menu!")

    def test_add_table(self):
        self.assertEqual(self.bakery.add_table("Inner",11,11), None)
        self.assertEqual(self.bakery.add_table("InsideTable",1,8),"Added table number 1 in the bakery")
        self.assertEqual(self.bakery.add_table("OutsideTable",51,11),"Added table number 51 in the bakery")
        with self.assertRaises(Exception) as exc:
            self.bakery.add_table("OutsideTable", 51, 11)
        self.assertEqual(str(exc.exception),"Table 51 is already in the bakery!")

    def test_reserve_table(self):
        self.bakery.add_table("OutsideTable",51,11)
        self.assertEqual(self.bakery.reserve_table(11),"Table 51 has been reserved for 11 people")
        self.assertEqual(self.bakery.reserve_table(111),"No available table for 111 people")

    def test_order_food(self):
        self.bakery.add_table("OutsideTable", 51, 11)
        self.bakery.add_food("Bread","Homemade", 11)
        self.bakery.add_food("Cake","Homemade cake", 18)
        self.assertEqual(self.bakery.order_food(1112),"Could not find table 1112")
        self.assertEqual(self.bakery.order_food(51,"milk shake","homemade","gingerbread"),"Table 51 ordered:\n\nMy bake does not have in the menu:\nmilk shake\nhomemade\ngingerbread")
        self.assertEqual(self.bakery.order_food(51,"milk shake","Homemade","gingerbread"),"Table 51 ordered:\n - Homemade: 200.00g - 11.00lv\nMy bake does not have in the menu:\nmilk shake\ngingerbread")
        self.assertEqual(self.bakery.order_food(51,"Homemade"),"Table 51 ordered:\n - Homemade: 200.00g - 11.00lv\nMy bake does not have in the menu:\n")

    def test_order_drink(self):
        self.bakery.add_table("OutsideTable", 51, 11)
        self.bakery.add_drink("Water", "Spring water", 11,"Waterfall")
        self.bakery.add_drink("Tea", "Herbal tea", 18, "TeaMount")
        self.assertEqual(self.bakery.order_drink(1154),"Could not find table 1154")
        self.assertEqual(self.bakery.order_drink(51, "milk shake", "homemade", "gingerbread"), "Table 51 ordered:\n\nMy bake does not have in the menu:\nmilk shake\nhomemade\ngingerbread")
        self.assertEqual(self.bakery.order_drink(51, "Herbal tea","No","Spring water"), "Table 51 ordered:\n - Herbal tea TeaMount - 18.00ml - 2.50lv\n - Spring water Waterfall - 11.00ml - 1.50lv\nMy bake does not have in the menu:\nNo")

    def test_leave_table(self):
        self.bakery.add_table("OutsideTable", 51, 11)
        self.bakery.add_drink("Water", "Spring water", 11, "Waterfall")
        self.bakery.add_drink("Tea", "Herbal tea", 18, "TeaMount")
        self.bakery.order_drink(51, "milk shake", "Herbal tea")
        self.assertEqual(self.bakery.leave_table(51), "Table: 51\nBill: 2.50")
        self.assertEqual(self.bakery.leave_table(51), "Table: 51\nBill: 0.00")
        self.assertEqual(self.bakery.leave_table(511), None)

    def test_get_free_tables_info(self):
        self.assertEqual("", self.bakery.get_free_tables_info())
        self.bakery.add_table("OutsideTable", 51, 11)
        self.assertEqual('Table: 51\nType: OutsideTable\nCapacity: 11', self.bakery.get_free_tables_info())

    def test_get_total_income(self):
        self.fail()

    def test_name(self):
        self.fail()

