from project.loans.base_loan import BaseLoan

class MortgageLoan(BaseLoan):

    def __init__(self):
        super().__init__(3.5, 50_000)

    def increase_interest_rate(self):
        self._increase_rate(0.5)

