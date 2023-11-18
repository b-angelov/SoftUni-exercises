from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.my_decorators import MyDecoratorsMxn as mdxn
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    ALLOWED_VEHICLE_TYPES = {"CargoVan":CargoVan, "PassengerCar":PassengerCar}

    def __init__(self):
        self.users: [User] = []
        self.vehicles: [BaseVehicle] = []
        self.routes: [Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = mdxn.get_from_collection("driving_license_number",driving_license_number,self.users)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.ALLOWED_VEHICLE_TYPES.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."
        vehicle: BaseVehicle = mdxn.get_from_collection("license_plate_number",license_plate_number,self.vehicles)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        self.vehicles.append(self.ALLOWED_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."


    def allow_route(self, start_point: str, end_point: str, length: float):
        route = next((route for route in self.routes if route.start_point == start_point and route.end_point == end_point and route.length == length), None)
        if route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        route = next((route for route in self.routes if route.start_point == start_point and route.end_point == end_point and route.length < length), None)
        if route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."
        route:Route = next((route for route in self.routes if route.start_point == start_point and route.end_point == end_point and route.length > length), None)
        if route:
            route.is_locked = True
        self.routes.append(Route(start_point,end_point,length,self.__route_id))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user:User = mdxn.get_from_collection("driving_license_number",driving_license_number,self.users)
        vehicle:BaseVehicle = mdxn.get_from_collection("license_plate_number",license_plate_number,self.vehicles)
        route:Route = mdxn.get_from_collection("route_id",route_id,self.routes)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles_list: [BaseVehicle] = self.get_from_collection("is_damaged",True,self.vehicles,False)
        vehicles_list.sort(key=lambda x: (x.brand,x.model))
        vehicles_list = vehicles_list[:count]
        for vehicle in vehicles_list:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(vehicles_list)} vehicles were successfully repaired!"

    def users_report(self, ):
        result = ["*** E-Drive-Rent ***"]
        users = sorted(self.users, key=lambda x: -x.rating)
        result.extend(str(user) for user in users)
        return '\n'.join(result)

    @property
    def __route_id(self):
        return len(self.routes) + 1

