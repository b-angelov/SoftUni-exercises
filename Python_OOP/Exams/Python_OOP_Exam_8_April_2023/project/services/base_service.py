from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @abstractmethod
    def details(self):
        """Returns a string with information about the service depending on its type."""
        ...

    def add_robot(self, robot):
        self.capacity -= 1
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)
        self.capacity += 1

    def feed_robots(self):
        for robot in self.robots:
            robot.eating()
        return len(self.robots)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Service name cannot be empty!")
        self.__name = name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity
        if 0 >= capacity:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

    @property
    def current_capacity(self):
        return self.capacity - len(self.robots)

