from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.software import Software
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.common_functions import *

class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware: Hardware = get_from_collection_or_error(System._hardware,"name",hardware_name,do_not_raise_error=True)
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name,capacity_consumption,memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware: Hardware = get_from_collection_or_error(System._hardware, "name", hardware_name,do_not_raise_error=True)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware:Hardware = get_from_collection_or_error(System._hardware,"name",hardware_name,do_not_raise_error=True)
        software:Software = get_from_collection_or_error(System._software,"name",software_name,do_not_raise_error=True)
        if not hardware or not software:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum(software.memory_consumption for software in System._software)} / {sum(software.memory_consumption for software in System._software) + sum(hardware.memory for hardware in System._hardware)}
Total Capacity Taken: {sum(software.capacity_consumption for software in System._software)} / {sum(software.capacity_consumption for software in System._software) + sum(hardware.capacity for hardware in System._hardware)}"""


    @staticmethod
    def system_split():
        out = [f"""Hardware Component - {hardware.name}
Express Software Components: {len(get_from_collection_or_error(hardware.software_components,"software_type","Express",do_not_raise_error=True,whole=True))}
Light Software Components: {len(get_from_collection_or_error(hardware.software_components,"software_type","Light",do_not_raise_error=True,whole=True))}
Memory Usage: {sum(software.memory_consumption for software in hardware.software_components)} / {sum(software.memory_consumption for software in hardware.software_components) + hardware.memory}
Capacity Usage: {sum(software.capacity_consumption for software in hardware.software_components)} / {sum(software.capacity_consumption for software in hardware.software_components) + hardware.capacity}
Type: {hardware.hardware_type}
Software Components: {', '.join(software.name for software in hardware.software_components) if hardware.software_components else 'None'}""" for hardware in System._hardware]
        return "\n".join(out)
