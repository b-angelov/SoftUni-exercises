from unittest import TestCase
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart("MyShop",8254.20)

    def test_init(self):
        self.assertEqual(self.cart.shop_name,"MyShop")
        self.assertEqual(self.cart.budget,8254.20)
        self.assertEqual(self.cart.products,{})

    def test_shop_name_valid(self):
        self.cart.shop_name = "MyNewShop"
        self.assertEqual(self.cart.shop_name,"MyNewShop")

    def test_shop_name_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.cart.shop_name = "nighterShop"
        self.assertEqual(str(msg.exception), "Shop must contain only letters and must start with capital letter!")
        with self.assertRaises(ValueError) as msg:
            self.cart.shop_name = 1841
        self.assertEqual(str(msg.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_cart_valid(self):
        self.assertEqual(self.cart.add_to_cart("water",1.54),f"water product was successfully added to the cart!")
        self.assertEqual(self.cart.products,{"water":1.54})

    def test_add_to_cart_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.cart.add_to_cart("water", 100)
        self.assertEqual(str(msg.exception), f"Product water cost too much!")
        self.assertEqual(self.cart.products, {})

    def test_remove_from_cart_valid(self):
        self.cart.add_to_cart("water",1.54)
        self.cart.add_to_cart("milk",2.4)
        self.assertEqual(self.cart.remove_from_cart("water"), f"Product water was successfully removed from the cart!")
        self.assertEqual(self.cart.products,{"milk":2.4})

    def test_remove_from_cart_invalid(self):
        with self.assertRaises(ValueError) as msg:
            self.cart.remove_from_cart("dustyWater")
        self.assertEqual(str(msg.exception),f"No product with name dustyWater in the cart!")

    def test_buy_products_valid(self):
        self.cart.budget = 121
        self.cart.add_to_cart("papers",95)
        self.cart.add_to_cart("ribbons",5)
        self.assertEqual(self.cart.buy_products(), f'Products were successfully bought! Total cost: {100:.2f}lv.')

    def test_buy_products_invalid(self):
        self.cart.budget = 91
        self.cart.add_to_cart("papers", 95)
        with self.assertRaises(ValueError) as msg:
            self.cart.buy_products()
        self.assertEqual(str(msg.exception),f"Not enough money to buy the products! Over budget with {95 - self.cart.budget:.2f}lv!")

    def test_add(self):
        self.cart.add_to_cart("milk",11)
        cart2 = ShoppingCart("Shoppie",214)
        cart2.add_to_cart("bread",4.2)
        new_cart = self.cart + cart2
        self.assertIsInstance(new_cart, ShoppingCart)
        self.assertEqual(new_cart.shop_name,"MyShopShoppie")
        self.assertEqual(new_cart.budget,self.cart.budget + cart2.budget)
        new_products = dict(self.cart.products, **cart2.products)
        self.assertEqual(new_cart.products,new_products)
