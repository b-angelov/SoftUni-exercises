from project.formula_teams.formula_team import FormulaTeam

class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors = {"Oracle": {1:1_500_000, 2:800_000},"Honda":{8:20_000,10:10_000}}
        expenses = 250_000
        revenue = self.sponsor_funds(race_pos,sponsors.get("Oracle").items())
        revenue += self.sponsor_funds(race_pos,sponsors.get("Honda").items())
        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"


