from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICES_AVAILABLE = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOTS_AVAILABLE = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICES_AVAILABLE.keys():
            raise Exception("Invalid service type!")
        self.services.append(self.SERVICES_AVAILABLE[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOTS_AVAILABLE.keys():
            raise Exception("Invalid robot type!")
        self.robots.append(self.ROBOTS_AVAILABLE[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = tuple(robot for robot in self.robots if robot.name == robot_name)[0]
        service = tuple(service for service in self.services if service.name == service_name)[0]
        robot_type = robot.__class__.__name__
        service_type = service.__class__.__name__
        if not ((robot_type == "FemaleRobot" and service_type == "SecondaryService") or (robot_type == "MaleRobot" and service_type == "MainService")):
            return "Unsuitable service."
        if not service.current_capacity:
            raise Exception("Not enough capacity for this robot!")
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = tuple(service for service in self.services if service.name == service_name)[0]
        robot = tuple(robot for robot in service.robots if robot.name == robot_name)
        if not robot:
            raise Exception("No such robot in this service!")
        robot = robot[0]
        service.remove_robot(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = service = tuple(service for service in self.services if service.name == service_name)[0]
        return f"Robots fed: {service.feed_robots()}."

    def service_price(self, service_name: str):
        service = tuple(service for service in self.services if service.name == service_name)[0]
        return f"The value of service {service_name} is {sum(robot.price for robot in service.robots):.2f}."

    def __str__(self):
        res = []
        for service in self.services:
            res.append(service.details())
        return '\n'.join(res)




