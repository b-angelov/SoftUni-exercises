from project.my_decorators import MyDecoratorsMxn as mdxn
class User:

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked: bool = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    @mdxn.check_str("First name cannot be empty!")
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    @mdxn.check_str("Last name cannot be empty!")
    def last_name(self, value):
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    @mdxn.check_str("Driving license number is required!")
    def driving_license_number(self, value):
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    @mdxn.check_int("Users rating cannot be negative!", 0)
    def rating(self, value):
        self.__rating = value

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10:
            self.rating = 10

    def decrease_rating(self):
        try:
            self.rating -= 2.0
        except ValueError:
            self.rating = 0
            self.is_blocked = True

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"
