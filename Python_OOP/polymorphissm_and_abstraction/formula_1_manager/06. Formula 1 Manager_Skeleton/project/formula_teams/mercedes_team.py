from project.formula_teams.formula_team import FormulaTeam

class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {"Petronas": {1:1_000_000, 3:500_000},"TeamViewer":{5:100_000,7:50_000}}
        expenses = 200_000
        revenue = self.sponsor_funds(race_pos, sponsors.get("Petronas").items())
        revenue += self.sponsor_funds(race_pos, sponsors.get("TeamViewer").items())
        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"