from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        reduction = 30 * 1.3 if peak.dificulty_level == "Advanced" else 30 * 2.5
        self.strength -= reduction
        self.conquered_peaks.append(peak.name)
