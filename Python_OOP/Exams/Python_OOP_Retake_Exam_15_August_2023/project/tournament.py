from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.my_decorators import MyDecoratorsMxn as mdxn
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    SUPPORTED_EQUIPMENTS = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: [BaseEquipment] = []
        self.teams: [BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    @property
    def __current_capacity(self):
        return self.capacity - len(self.teams)

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.SUPPORTED_EQUIPMENTS.keys():
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.SUPPORTED_EQUIPMENTS[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES.keys():
            raise Exception("Invalid team type!")
        if not self.__current_capacity:
            return "Not enough tournament capacity."
        self.teams.append(self.TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment: BaseEquipment = next(eq for eq in reversed(self.equipment) if eq.__class__.__name__ == equipment_type)
        team: BaseTeam = mdxn.get_from_collection("name", team_name, self.teams)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team: BaseTeam = mdxn.get_from_collection_or_raise("name", team_name, self.teams, message="No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipments_increased = len(
            [eq.increase_price() for eq in self.equipment if equipment_type == eq.__class__.__name__])
        return f"Successfully changed {equipments_increased}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1: BaseTeam = mdxn.get_from_collection("name", team_name1, self.teams)
        team2: BaseTeam = mdxn.get_from_collection("name", team_name2, self.teams)
        if type(team1) != type(team2):
            raise Exception("Game cannot start! Team types mismatch!")
        if team1.team_score == team2.team_score:
            return "No winner in this game."
        winner, loser = sorted((team1, team2), key=lambda x: -x.team_score)
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self, ):
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:"
                  ]
        teams = sorted(self.teams, key=lambda x: -x.wins)
        result.extend(team.get_statistics() for team in teams)
        return "\n".join(result)
