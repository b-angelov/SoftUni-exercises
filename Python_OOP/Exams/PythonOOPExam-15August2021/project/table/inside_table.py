from project.table.table import Table
from project.common_functions import exc

class InsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        super().__init__(self.table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number
    @table_number.setter
    def table_number(self, table_number: int):
        exc("Inside table's number must be between 1 and 50 inclusive!", table_number not in range(1,51))
        self.__table_number = table_number