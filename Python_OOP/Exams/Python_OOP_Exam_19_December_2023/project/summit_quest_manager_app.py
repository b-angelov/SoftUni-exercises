from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitQuestManagerApp:

    def __init__(self):
        climbers: [BaseClimber] = []
        peaks: [BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        pass

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        pass

    def check_gear(self, climber_name: str, peak_name: str, gear: [str]):
        pass

    def perform_climbing(self, climber_name: str, peak_name: str):
        pass

    def get_statistics(self ):
        pass
