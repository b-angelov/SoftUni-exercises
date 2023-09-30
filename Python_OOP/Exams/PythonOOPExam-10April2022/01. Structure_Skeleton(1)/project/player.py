from project.supply.supply import exc
# from supply.supply import exc
# from controller import _check_collections

class Player:

    player_list = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        exc("Name not valid!",not name)
        if name in self.player_list:
            raise Exception(f"Name {name} is already used!")
        self.__name = name
        self.player_list.append(name)

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        exc("The player cannot be under 12 years old!", age < 12)
        self.__age = age

    @property
    def stamina(self):
        return self.__stamina
    @stamina.setter
    def stamina(self, stamina:int):
        exc("Stamina not valid!", 0 > stamina or stamina > 100)
        self.__stamina = stamina
        if self.__stamina < 0:
            self.__stamina = 0

    @property
    def need_sustenance(self):
        return self.stamina < 100

