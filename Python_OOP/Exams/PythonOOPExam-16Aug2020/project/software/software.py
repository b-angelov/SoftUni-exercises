from abc import ABC

class Software(ABC):

    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        self.name: str = name
        self.software_type: str = software_type
        self.capacity_consumption: int = capacity_consumption
        self.memory_consumption: int = memory_consumption


