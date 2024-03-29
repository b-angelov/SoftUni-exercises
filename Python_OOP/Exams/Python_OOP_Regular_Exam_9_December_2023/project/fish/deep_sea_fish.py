from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):

    def __init__(self, name: str, points: float):
        super().__init__(name, points, 180)

    def fish_details(self):
        return self._display_details()
