from project.planet.planet import Planet
from project.common_functions import get_from_collection_or_error

class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        return get_from_collection_or_error(self.planets,"name",name,do_not_raise_error=True) or None