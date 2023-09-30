from project.astronaut.astronaut import Astronaut
from project.common_functions import get_from_collection_or_error

class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        return get_from_collection_or_error(self.astronauts,"name",name,do_not_raise_error=True) or None