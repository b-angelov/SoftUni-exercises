from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    type_oxygen_level = 540

    def __init__(self, name: str):
        super().__init__(name, self.type_oxygen_level)

    def miss(self, time_to_catch: int):
        time_to_catch = round(time_to_catch * 0.3)
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
            return
        self.oxygen_level -= time_to_catch

    def renew_oxy(self):
        self.oxygen_level = self.type_oxygen_level