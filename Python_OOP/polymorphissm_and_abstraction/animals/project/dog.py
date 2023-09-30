from project.animal import Animal


class Dog(Animal):

    __sound = "Woof!"

    @classmethod
    def make_sound(cls):
        return Dog.__sound

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
