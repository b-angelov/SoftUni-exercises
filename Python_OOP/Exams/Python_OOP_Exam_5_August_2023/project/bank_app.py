from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    SUPPORTED_LOANS: {str: BaseLoan} = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    SUPPORTED_CLIENTS: {str: BaseClient} = {"Student": Student, "Adult": Adult}
    PERMITTED_LOANS: {str: str} = dict(zip(SUPPORTED_CLIENTS.keys(), SUPPORTED_LOANS.keys()))

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: [BaseLoan] = []
        self.clients: [BaseClient] = []

    @property
    def __remaining_space(self):
        return self.capacity - len(self.clients)

    def __get_client_by_id(self, client_id: str) -> BaseClient:
        return next((client for client in self.clients if client.client_id == client_id), None)

    def __get_loan_by_type(self, loan_type: str) -> BaseLoan:
        return next((loan for loan in self.loans if loan.__class__.__name__ == loan_type), None)

    def add_loan(self, loan_type: str):
        if loan_type not in self.SUPPORTED_LOANS.keys():
            raise Exception("Invalid loan type!")
        self.loans.append(self.SUPPORTED_LOANS[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.SUPPORTED_CLIENTS.keys():
            raise Exception("Invalid client type!")
        if not self.__remaining_space:
            return "Not enough bank capacity."
        self.clients.append(self.SUPPORTED_CLIENTS[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan: BaseLoan = self.__get_loan_by_type(loan_type)
        client: BaseClient = self.__get_client_by_id(client_id)
        if self.PERMITTED_LOANS[client.__class__.__name__] != loan_type:
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.__get_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = len(
            [loan.increase_interest_rate() for loan in self.loans if loan.__class__.__name__ == loan_type])
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = len(
            [client.increase_clients_interest() for client in self.clients if client.interest < min_rate])
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {sum(client.income for client in self.clients):.2f}\n" \
               f"Granted Loans: {sum(len(client.loans) for client in self.clients)}, Total Sum: {sum(sum(loan.amount for loan in client.loans) for client in self.clients):.2f}\n" \
               f"Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}\n" \
               f"Average Client Interest Rate: {(sum(client.interest for client in self.clients) / len(self.clients)) if self.clients else 0:.2f}"
