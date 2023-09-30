from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam

class F1SeasonApp:

    teams = {"Red Bull":RedBullTeam,"Mercedes":MercedesTeam}

    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.teams.keys():
            raise ValueError("Invalid team name!")
        self.__setattr__(team_name.lower().replace(" ","_") + "_team", self.teams[team_name](budget))
        return f"{ team_name } has joined the new F1 season."

    def  new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not all((self.red_bull_team,self.mercedes_team)):
            raise Exception("Not all teams have registered for the season.")
        better = min(zip(self.teams.keys(),(red_bull_pos,mercedes_pos)), key = lambda x: x[1])
        return f"Red Bull: { self.red_bull_team.calculate_revenue_after_race(red_bull_pos) }. Mercedes: { self.mercedes_team.calculate_revenue_after_race(mercedes_pos) }. { better[0] } is ahead at the { race_name } race."
