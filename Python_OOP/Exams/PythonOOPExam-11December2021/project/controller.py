from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race
from project.common_functions import *

class Controller:

    CAR_TYPES = {"MuscleCar":MuscleCar, "SportsCar":SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.CAR_TYPES.keys():
            return
        check_collections(
            collection=self.cars,
            attr="model", name=model,
            error_message=f"Car {model} is already created!"
        )
        self.cars.append(self.CAR_TYPES[car_type](model, speed_limit))
        return f"{car_type} {model} is created."


    def create_driver(self, driver_name: str):
        check_collections(
            collection=self.drivers,
            attr="name", name=driver_name,
            error_message=f"Driver {driver_name} is already created!"
        )
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."


    def create_race(self, race_name: str):
        check_collections(
            collection=self.races,
            attr="name", name=race_name,
            error_message=f"Race {race_name} is already created!"
        )
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."



    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__is_driver_present(driver_name)
        car = check_collections(
            collection=self.cars,
            attr="car_type", name=car_type, item=-1,
            attr1="is_taken", name1=False,
            error_raise_condition=False,error_message=f"Car {car_type} could not be found!"
        )
        driver_has_a_car = driver.car
        driver.car = car
        car.is_taken = driver
        if driver_has_a_car:
            driver_has_a_car.is_taken = None
            return f"Driver {driver_name} changed his car from {driver_has_a_car.model} to {car.model}."
        return f"Driver {driver_name} chose the car {car.model}."


    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__is_race_present(race_name)
        driver = self.__is_driver_present(driver_name)
        exc(f"Driver {driver_name} could not participate in the race!",not driver.car, Exception)
        is_added = check_collections(
            collection=race.drivers,
            attr="name", name=driver_name,
            do_not_raise_error=True
        )
        if is_added:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."


    def start_race(self, race_name: str):
        race = self.__is_race_present(race_name)
        exc(f"Race {race_name} cannot start with less than 3 participants!",len(race.drivers) < 3,Exception)
        race.drivers.sort(key= lambda driver: -driver.car.speed_limit)
        winners = race.drivers[:3]
        def set_winner(driver):
            driver.number_of_wins += 1
        set(map(set_winner, winners))
        return "\n".join(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}." for driver in winners)


    def __is_driver_present(self, name):
        return  check_collections(
            collection=self.drivers,
            attr="name", name=name,
            error_raise_condition=False,error_message=f"Driver {name} could not be found!"
        )
    def __is_race_present(self, name):
        return  check_collections(
            collection=self.races,
            attr="name", name=name,
            error_raise_condition=False,error_message=f"Race {name} could not be found!"
        )
