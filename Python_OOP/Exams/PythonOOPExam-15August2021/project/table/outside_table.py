from project.table.table import Table
from project.common_functions import exc

class OutsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        super().__init__(self.table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number
    @table_number.setter
    def table_number(self, table_number: int):
        exc("Outside table's number must be between 51 and 100 inclusive!", table_number not in range(51,101))
        self.__table_number = table_number