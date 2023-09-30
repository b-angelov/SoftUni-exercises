from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.base_decoration import BaseDecoration
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.decoration.decoration_repository import DecorationRepository
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.common_functions import *

class Controller:

    AQUARIUM_TYPES = {"FreshwaterAquarium":FreshwaterAquarium, "SaltwaterAquarium":SaltwaterAquarium}
    FISH_TYPES = {"FreshwaterFish":FreshwaterFish, "SaltwaterFish":SaltwaterFish}
    ORNAMENT_TYPES = {"Plant":Plant, "Ornament":Ornament}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.AQUARIUM_TYPES.keys():
            return "Invalid aquarium type."
        self.aquariums.append(self.AQUARIUM_TYPES[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."


    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.ORNAMENT_TYPES.keys():
            return "Invalid decoration type."
        self.decorations_repository.add(self.ORNAMENT_TYPES[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium: BaseAquarium = self.__get_aquarium(aquarium_name)
        # if not aquarium:
        #     return
        decoration: BaseDecoration = self.decorations_repository.find_by_type(decoration_type)
        self.decorations_repository.remove(decoration)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium:BaseAquarium = self.__get_aquarium(aquarium_name)
        if not aquarium:
            return
        if fish_type not in self.FISH_TYPES.keys():
            return f"There isn't a fish of type {fish_type}."
        fish: BaseFish = self.FISH_TYPES[fish_type](fish_name,fish_species,price)
        if fish.habitat != aquarium.__class__.__name__:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium:BaseAquarium = self.__get_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium:BaseAquarium = self.__get_aquarium(aquarium_name)
        value = sum(decoration.price for decoration in aquarium.decorations) + sum(fish.price for fish in aquarium.fish)
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return "\n".join(aquarium.__str__() for aquarium in self.aquariums)

    def __get_aquarium(self, aquarium_name):
        return get_from_collection_or_error(self.aquariums,"name",aquarium_name,do_not_raise_error=True)