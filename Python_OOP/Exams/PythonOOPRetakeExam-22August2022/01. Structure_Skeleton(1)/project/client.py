from re import match

class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, number: str):
        if not match(r"^0{1}\d{9}$", number):
            raise ValueError("Invalid phone number!")
        self._phone_number = number

    # @property
    # def shopping_cart(self):
    #     return self._shopping_cart
    # @shopping_cart.setter
    # def shopping_cart(self, value: object):
    #     if not value:
    #         self._shopping_cart = []
    #     else:
    #         self._shopping_cart.append(value)
    #         self.bill += value.price

