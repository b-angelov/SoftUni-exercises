from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    ALLOWED_DIVERS = {"ScubaDiver":ScubaDiver, "FreeDiver":FreeDiver}
    ALLOWED_FISH = {"DeepSeaFish":DeepSeaFish, "PredatoryFish":PredatoryFish}

    def __init__(self):
        self.divers: [BaseDiver] = []
        self.fish_list: [BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.ALLOWED_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        if diver_name in (diver.name for diver in self.divers):
            return f"{diver_name} is already a participant."
        diver: BaseDiver = self.ALLOWED_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.ALLOWED_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        if fish_name in (fish.name for fish in self.fish_list):
            return f"{fish_name} is already permitted."
        fish = self.ALLOWED_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}." #one space removed from the beginning, it may fail if required

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver:BaseDiver = next((diver for diver in self.divers if diver.name == diver_name),None)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        fish: BaseFish = next((fish for fish in self.fish_list if fish.name == fish_name),None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                divers_count += 1
                diver.update_health_status()
                diver.renew_oxy()
        return f"Divers recovered: {divers_count}"


    def diver_catch_report(self, diver_name: str):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if not diver:
            return
        res = [
            f"**{diver_name} Catch Report**"
        ]
        res.extend(fish.fish_details() for fish in diver.catch)
        return "\n".join(res)

    def competition_statistics(self, ):
        res = [f"**Nautical Catch Challenge Statistics**"]
        divers = filter(lambda x: not x.has_health_issue, self.divers)
        divers = sorted(divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        res.extend(str(diver) for diver in divers)
        return "\n".join(res)
