from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish
from project.helper import *


class NauticalCatchChallengeApp:
    ALLOWED_DIVERS = {"ScubaDiver": ScubaDiver, "FreeDiver": FreeDiver}
    ALLOWED_FISH = {"DeepSeaFish": DeepSeaFish, "PredatoryFish": PredatoryFish}

    def __init__(self):
        self.divers: [BaseDiver] = []
        self.fish_list: [BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.ALLOWED_DIVERS:
            return f"{diver_type} is not allowed in our competition."
        diver = is_in_collection("name", diver_name, self.divers, None)
        if diver:
            return f"{diver_name} is already a participant."
        diver = self.ALLOWED_DIVERS[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.ALLOWED_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."
        fish = is_in_collection("name", fish_name, self.fish_list, None)
        if fish:
            return f"{fish_name} is already permitted."
        fish = self.ALLOWED_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver: BaseDiver = self.__get_diver(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        fish: BaseFish = self.__get_fish(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."


    def health_recovery(self, ):
        count = 0
        for diver in self.divers:
            diver: BaseDiver
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.__get_diver(diver_name)
        if not diver:
            return
        res = [f"**{diver_name} Catch Report**"]
        res.extend(fish.fish_details() for fish in diver.catch)
        return '\n'.join(res)

    def competition_statistics(self, ):
        divers = filter(lambda diver: not diver.has_health_issue, self.divers)
        divers: [BaseDiver] = sorted(divers, key=lambda diver: (-diver.competition_points,-len(diver.catch),diver.name))
        res = [f"**Nautical Catch Challenge Statistics**"]
        res.extend(str(diver) for diver in divers)
        return '\n'.join(res)

    def __get_diver(self, name):
        return is_in_collection("name",name,self.divers, None)

    def __get_fish(self, name):
        return is_in_collection("name", name, self.fish_list, None)




