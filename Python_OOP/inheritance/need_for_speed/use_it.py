from project.vehicle import Vehicle
from project.family_car import FamilyCar
from project.sport_car import SportCar
from project.cross_motorcycle import CrossMotorcycle
from project.race_motorcycle import RaceMotorcycle

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(CrossMotorcycle.DEFAULT_FUEL_CONSUMPTION)
print(SportCar.DEFAULT_FUEL_CONSUMPTION)
print(RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
print(vehicle.fuel)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
