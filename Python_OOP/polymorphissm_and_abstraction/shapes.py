from abc import ABC,abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2 * pi

    def calculate_perimeter(self):
        return self.__radius * 2 * pi

class Rectangle(Shape):
    def __init__(self,height,width):
        self.__height,self.__width = height,width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return self.__height * 2 + self.__width * 2

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())


