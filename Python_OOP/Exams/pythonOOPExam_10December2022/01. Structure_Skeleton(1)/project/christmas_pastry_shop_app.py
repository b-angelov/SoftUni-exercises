from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.delicacy_names = []
        self.booth_numbers = []
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in self.delicacy_names:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.DELICACIES.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.DELICACIES[type_delicacy](name, price))
        self.delicacy_names.append(name)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in self.booth_numbers:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.BOOTHS.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.BOOTHS[type_booth](booth_number, capacity))
        self.booth_numbers.append(booth_number)
        return f"Added booth number {booth_number} in the pastry shop."

    def __find_appropriate_booth(self, people):
        booth = [booth for booth in self.booths if booth.is_reserved == False and booth.capacity >= people]
        if not booth:
            raise Exception(f"No available booth for {people} people!")
        return booth[0]

    def __find_delicacy(self, delicacy_name):
        delicacy = [delicacy for delicacy in self.delicacies if delicacy_name == delicacy.name]
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        return delicacy[0]

    def __find_booth_number(self, booth_number):
        booth = [booth for booth in self.booths if booth.booth_number == booth_number]
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        return booth[0]

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_appropriate_booth(number_of_people)
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_number(booth_number)
        delicacy = self.__find_delicacy(delicacy_name)

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_number(booth_number)
        bill = sum(order.price for order in booth.delicacy_orders) + booth.price_for_reservation
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        return f"Booth {booth_number}:\n" + \
            f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
