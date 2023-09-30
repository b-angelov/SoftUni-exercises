
class ImageArea:

    def __init__(self,*args: int):
        self.width,self.height = args

    def get_area(self):
        return self.width * self.height

    def __eq__(self, another):
        return self.get_area() == another

    def __lt__(self, another):
        return self.get_area() < another

    def __le__(self, another):
        return self.get_area() <= another

    def __gt__(self, another):
        return self.get_area() > another

    def __ge__(self, another):
        return self.get_area() >= another

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)


