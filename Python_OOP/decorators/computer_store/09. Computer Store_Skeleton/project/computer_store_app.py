from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

class ComputerStoreApp:

    computers = {"Desktop Computer":DesktopComputer,"Laptop":Laptop}

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.computers.keys():
            raise ValueError(f"{ type_computer } is not a valid type computer!")
        computer = self.computers[type_computer](manufacturer, model)
        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration


    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = [computer for computer in self.warehouse if computer.price <= client_budget and wanted_processor == computer.processor and wanted_ram <= computer.ram]
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")
        computer = computer[0]
        self.warehouse.remove(computer)
        profit = client_budget - computer.price
        self.profits += profit
        return f"{ computer } sold for { client_budget }$."