from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    initial_oxygen = 120

    def __init__(self, name: str):
        super().__init__(name, self.initial_oxygen)

    def miss(self, time_to_catch: int):
        self._miss(time_to_catch, 0.6)

    def renew_oxy(self):
        self._renew_oxygen(self.initial_oxygen)