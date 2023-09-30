from project.computer_types.computer import Computer

class Laptop(Computer):
    available_processors = {"AMD Ryzen 9 5950X": 900,"Intel Core i9-11900H": 1050,"Apple M1 Pro": 1200}

    def __init__(self, manufacturer: str, model: str):

        super().__init__(manufacturer, model)

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, value):
        if value != None and value not in self.available_processors.keys():
            raise ValueError(f"{ value } is not compatible with laptop { self.manufacturer } { self.model }!")
        self.__processor = value
        
    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        if value != None and value not in (2 ** i for i in range(1,7)):
            raise ValueError(f"{ value }GB RAM is not compatible with laptop { self.manufacturer } { self.model }!")
        self.__ram = value

    def configure_computer(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price = self.available_processors[processor] + (sum(self._power_of_two(ram)) * 100)
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."



