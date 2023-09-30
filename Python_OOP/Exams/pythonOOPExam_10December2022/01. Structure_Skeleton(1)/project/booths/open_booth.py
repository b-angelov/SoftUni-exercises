from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)
        self.booth_number = booth_number
        self.capacity = capacity

    def reserve(self, number_of_people: int):
        price = number_of_people * self.PRICE_PER_PERSON
        self.is_reserved = price
