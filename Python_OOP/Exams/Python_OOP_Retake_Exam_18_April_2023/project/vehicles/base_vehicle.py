from abc import ABC, abstractmethod
from project.my_decorators import MyDecoratorsMxn as mdxn


class BaseVehicle(ABC):

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level: int = 100
        self.is_damaged: bool = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    @mdxn.check_str("Brand cannot be empty!")
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    @mdxn.check_str("Model cannot be empty!")
    def model(self, value):
        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    @mdxn.check_str("License plate number is required!")
    def license_plate_number(self, value):
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} "\
        f"Battery: {self.battery_level}% Status: {'OK' if not self.is_damaged else 'Damaged'}"
