from abc import ABC
from project.software.software import Software
from project.common_functions import exc, remove_from_collection_or_error

class Hardware(ABC):

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name: str =name
        self.hardware_type: str = hardware_type
        self.capacity: int = capacity
        self.memory: int = memory
        self.software_components: list = []


    def install(self, software: Software):
        exc("Software cannot be installed", software.capacity_consumption > self.capacity or software.memory_consumption > self.memory, Exception)
        self.capacity -= software.capacity_consumption
        self.memory -= software.memory_consumption
        self.software_components.append(software)

    def uninstall(self, software: Software):
        try:
            remove_from_collection_or_error(self.software_components,"name",software.name)
            self.memory += software.memory_consumption
            self.capacity += software.capacity_consumption
        except:
            pass
