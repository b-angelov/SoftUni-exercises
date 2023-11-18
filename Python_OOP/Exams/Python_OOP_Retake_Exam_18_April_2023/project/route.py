from project.my_decorators import MyDecoratorsMxn as mdxn

class Route:

    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked: bool = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    @mdxn.check_str("Start point cannot be empty!")
    def start_point(self, value):
        self.__start_point = value


    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    @mdxn.check_str("End point cannot be empty!")
    def end_point(self, value):
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    @mdxn.check_int("Length cannot be less than 1.00 kilometer!",1.00)
    def length(self, value):
        self.__length = value
