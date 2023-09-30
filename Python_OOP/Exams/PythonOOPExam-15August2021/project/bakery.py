from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table
from project.common_functions import *

class Bakery:

    FOOD_TYPES,DRINK_TYPES = {"Bread":Bread, "Cake":Cake,},{"Tea":Tea, "Water":Water,}
    TABLE_TYPES = {"InsideTable":InsideTable, "OutsideTable":OutsideTable}

    def __init__(self,name: str):
        self.name = name
        self.food_menu,self.drinks_menu = [],[]
        self.tables_repository = []
        self.total_income = 0.0

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in self.FOOD_TYPES.keys():
            return
        not_in_collection_or_error(self.food_menu,"name",name,f"{food_type} {name} is already in the menu!")
        self.food_menu.append(self.FOOD_TYPES[food_type](name,price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in self.DRINK_TYPES.keys():
            return
        not_in_collection_or_error(self.drinks_menu, "name", name, f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(self.DRINK_TYPES[drink_type](name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self.TABLE_TYPES.keys():
            return
        not_in_collection_or_error(self.tables_repository,"table_number",table_number,f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(self.TABLE_TYPES[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table: Table = get_from_collection_or_error(self.tables_repository,"is_reserved",False,do_not_raise_error=True,attr1="capacity",name1=number_of_people,op2=">=")
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *foods):
        table: Table = get_from_collection_or_error(self.tables_repository,"table_number",table_number,do_not_raise_error=True)
        if not table:
            return f"Could not find table {table_number}"
        foods_order = {"added":[],"not added":[]}
        for food in foods:
            add = get_from_collection_or_error(self.food_menu,"name",food,do_not_raise_error=True)
            if add:
                table.order_food(add)
                foods_order["added"].append(add)
            else:
                foods_order["not added"].append(food)
        not_added = f"\n{self.name} does not have in the menu:\n"
        if foods_order["not added"]:
            not_added += '\n'.join(foods_order["not added"])
        return f"Table {table_number} ordered:\n" + "\n".join(food.__repr__() for food in foods_order["added"]) + not_added

    def order_drink(self, table_number: int, *drinks):
        table: Table = get_from_collection_or_error(self.tables_repository, "table_number", table_number,do_not_raise_error=True)
        if not table:
            return f"Could not find table {table_number}"
        drinks_order = {"added": [], "not added": []}
        for drink in drinks:
            add = get_from_collection_or_error(self.drinks_menu, "name", drink, do_not_raise_error=True)
            if add:
                table.order_drink(add)
                drinks_order["added"].append(add)
            else:
                drinks_order["not added"].append(drink)

        not_added = f"\n{self.name} does not have in the menu:\n"
        if drinks_order["not added"]:
            not_added += '\n'.join(drinks_order["not added"])
        return f"Table {table_number} ordered:\n" + "\n".join(drink.__repr__() for drink in drinks_order["added"]) + not_added

    def leave_table(self, table_number: int):
        table: Table = get_from_collection_or_error(self.tables_repository,"table_number",table_number,do_not_raise_error=True)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            message =  f"Table: {table_number}\n"+\
                    f"Bill: {bill:.2f}"
            table.clear()
            return message


    def get_free_tables_info(self):
        info = [table.free_table_info() for table in self.tables_repository]
        return "\n".join(list(filter(lambda x: x,info)))


    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
        # return f"Total income: {sum(table.get_bill() for table in self.tables_repository):.2f}lv"


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        exc("Name cannot be empty string or white space!",not name.strip())
        self.__name = name