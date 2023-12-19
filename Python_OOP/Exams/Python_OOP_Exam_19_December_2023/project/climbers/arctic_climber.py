from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        reduction = 20 * 2 if peak.dificulty_level == "Extreme" else 20 * 1.5
        self.strength -= reduction
        self.conquered_peaks.append(peak.name)
