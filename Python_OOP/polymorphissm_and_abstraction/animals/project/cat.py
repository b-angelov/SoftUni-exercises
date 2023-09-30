from project.animal import Animal


class Cat(Animal):

    __sound = "Meow meow!"

    @classmethod
    def make_sound(cls):
        return cls.__sound

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

