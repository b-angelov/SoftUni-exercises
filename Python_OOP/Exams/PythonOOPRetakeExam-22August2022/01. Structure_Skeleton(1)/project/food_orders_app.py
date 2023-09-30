from project.meals.dessert import Dessert
# from meals.dessert import Dessert
from project.meals.main_dish import MainDish
# from meals.main_dish import MainDish
from project.meals.starter import Starter
# from meals.starter import Starter
from project.client import Client
# from client import Client
from project.meals.meal import Meal
# from meals.meal import Meal
from copy import copy

class FoodOrdersApp:

    MEAL_TYPES = {"Dessert":Dessert,"MainDish":MainDish,"Starter":Starter}
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        self.__client_list_check_duplicates(client_phone_number)
        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.MEAL_TYPES.keys():
                self.menu.append(meal)

    def show_menu(self):
        self.__is_menu_ready()
        return "\n".join(list(meal.details() for meal in self.menu))

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__is_menu_ready()
        if not self.__is_client_registered(client_phone_number):
            self.register_client(client_phone_number)
        for meal in meal_names_and_quantities.items():
            self.__is_meal_quantity_sufficient(*meal)
        client = self.__get_client(client_phone_number)
        for nq in meal_names_and_quantities.items():
            name,quantity = nq
            meal = self.__get_meal(name)
            meal.quantity -= quantity
            # client.shopping_cart = self.MEAL_TYPES[meal.__class__.__name__](name,meal.price,quantity)
            client_meal = copy(meal)
            client_meal.quantity = quantity
            client.shopping_cart.append(client_meal)
            client.bill += quantity * meal.price
        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for meal in client.shopping_cart:
            menu_meal = self.__get_meal(meal.name)
            menu_meal.quantity += meal.quantity
        client.shopping_cart.clear()
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        client.shopping_cart = []
        paid = client.bill
        client.bill = 0
        return f"Receipt #{self.__next__()} with total amount of {paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __is_client_registered(self, phone_number):
        return any(client.phone_number == phone_number for client in self.clients_list)

    def __client_list_check_duplicates(self, phone_number: str):
        is_in = self.__is_client_registered(phone_number)
        if is_in:
            raise Exception("The client has already been registered!")

    def __is_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __is_meal_in_menu(self, meal):
        res = any(meal_menu.name == meal for meal_menu in self.menu)
        if not res: raise Exception(f"{meal} is not on the menu!")

    def __is_meal_quantity_sufficient(self, *meal_and_quantity):
        meal,quantity = meal_and_quantity
        self.__is_meal_in_menu(meal)
        meal = self.__get_meal(meal)
        if meal.quantity < quantity:
            raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

    def __get_meal(self, meal):
        return [meal_menu for meal_menu in self.menu if meal_menu.name == meal][0]

    def __get_client(self, phone_number):
        return [client for client in self.clients_list if client.phone_number == phone_number][0]

    def __next__(self):
        self.receipt_id += 1
        return self.receipt_id



