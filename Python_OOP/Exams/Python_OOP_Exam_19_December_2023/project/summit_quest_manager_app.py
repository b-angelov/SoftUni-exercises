from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    ALLOWED_CLIMBERS = {"ArcticClimber":ArcticClimber,"SummitClimber":SummitClimber}
    ALLOWED_PEAKS = {"ArcticPeak":ArcticPeak,"SummitPeak":SummitPeak}

    def __init__(self):
        self.climbers: [BaseClimber] = []
        self.peaks: [BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.ALLOWED_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."
        if next((climber.name for climber in self.climbers if climber.name == climber_name), None):
            return f"{climber_name} has been already registered."
        self.climbers.append(self.ALLOWED_CLIMBERS[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.ALLOWED_PEAKS:
            return f"{peak_type} is an unknown type of peak."
        self.peaks.append(self.ALLOWED_PEAKS[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: [str]):
        climber: BaseClimber = next((climber for climber in self.climbers if climber.name == climber_name), None)
        peak: BasePeak = next((peak for peak in self.peaks if peak.name == peak_name), None)
        if not set(peak.get_recommended_gear()).issubset(gear):
            climber.is_prepared = False
            missing_items = sorted(set(peak.get_recommended_gear()).difference(gear))
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_items)}."
        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber: BaseClimber = next((climber for climber in self.climbers if climber.name == climber_name), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        peak: BasePeak = next((peak for peak in self.peaks if peak.name == peak_name), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        if climber.can_climb():
            return f"{climber_name} will need to be better prepared next time."
        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers = filter(lambda climber: len(climber.conquered_peaks) > 0, self.climbers)
        climbers = sorted(climbers,key=lambda climber: (-len(climber.conquered_peaks), climber.name))
        res = [f"Total climbed peaks: {len(set(peak for climber in climbers for peak in climber.conquered_peaks))}", "**Climber's statistics:**"]
        res.extend(str(climber) for climber in climbers)
        return "\n".join(res)
