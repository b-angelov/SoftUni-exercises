
class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if not self.health:
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health: int):
        self.__health = health
        if self.__health < 0:
            self.health = 0

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
