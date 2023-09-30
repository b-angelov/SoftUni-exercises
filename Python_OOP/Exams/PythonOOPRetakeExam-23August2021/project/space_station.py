from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.common_functions import *


class SpaceStation:
    ASTRONAUT_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.missions = {"successful":0,"non successful":0}

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.ASTRONAUT_TYPES.get(astronaut_type)
        if not astronaut:
            raise Exception("Astronaut type is not valid!")
        if is_in_collection(self.astronaut_repository.astronauts, "name", name):
            return f"{name} is already added."
        self.astronaut_repository.add(astronaut(name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if is_in_collection(self.planet_repository.planets, "name", name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        remove_from_collection_or_error(self.astronaut_repository.astronauts, "name", name, f"Astronaut {name} doesn't exist!")
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        def recharge(astronaut):
            astronaut.increase_oxygen(10)

        set(map(recharge, self.astronaut_repository.astronauts))

    def send_on_mission(self, planet_name: str):
        planet = get_from_collection_or_error(self.planet_repository.planets,"name",planet_name,"Invalid planet name!")
        astronauts = get_from_collection_or_error(self.astronaut_repository.astronauts,"oxygen",30,whole=True,do_not_raise_error=True,op=">=")
        exc("You need at least one astronaut to explore the planet!",not astronauts,Exception)
        astronauts = sorted(astronauts,key=lambda astronaut: -astronaut.oxygen)[:5]
        for n,astronaut in enumerate(astronauts):
            self.__collect(astronaut,planet)
            if not planet.items:
                self.missions["successful"] += 1
                return f"Planet: {planet_name} was explored. {n+1} astronauts participated in collecting items."
        self.missions["non successful"] += 1
        return "Mission is not completed."


    def report(self):
        astronauts = "\n".join(astronaut.condition() for astronaut in self.astronaut_repository.astronauts)
        return f"{self.missions['successful']} successful missions!\n" +\
                f"{self.missions['non successful']} missions were not completed!\n"+\
                f"Astronauts' info:\n"+\
                f"{astronauts}"

    def __collect(self, astronaut: Astronaut, planet: Planet):
        while astronaut.oxygen > 0 and planet.items:
            astronaut.backpack.append(planet.items.pop())
            astronaut.breathe()
