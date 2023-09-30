from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table
from project.bakery import Bakery
from project.common_functions import *
# zip_current_project()

my_bread = Bread("home made",1)
print(my_bread)
my_cake = Cake("homemade cake",11)
print(my_cake)
my_water = Water("spring water",411,"Waterlands")
print(my_water)
my_tea = Tea("herbal tea",115,"MountainSprings")
print(my_tea)
table_1 = InsideTable(50,11)
table_2 = InsideTable(1,11)
table_3 = OutsideTable(51,11)
table_4 = OutsideTable(100,11)
table_1.capacity = 841211
# table_1.reserve(851)
print(table_1.get_bill())
print(table_1.free_table_info(),table_2.free_table_info(),table_3.free_table_info(),table_4.free_table_info(),sep="\n")

sep("bakery",symbols=50)
sep("add food")
bakery = Bakery("BakerLands-Nature")
print(bakery.add_food("Cake","Milk dropperies",811.22))
print(bakery.add_food("Cake","Regular cake",11.20))
print(bakery.add_food("Cake","Extraordinary cake",0.51))
print(bakery.add_food("Bread","Silk dropperies",811.22))
print(bakery.add_food("Bread","Homemade bread",11.0214))
# print(bakery.add_food("Bread","Silk dropperies",811.22))
sep("add drink")
print(bakery.add_drink("Water","Snowy water",841,"SnowMount"))
print(bakery.add_drink("Water","Salty water",841,"SpicyDrinks"))
print(bakery.add_drink("Tea","White-yellowish tea",60,"YellowSnows"))
print(bakery.add_drink("Tea","Purple tea",61,"YellowSnows"))
print(bakery.add_drink("Tea","Regular tea",11,"DeliciousDrinksCo"))
# bakery.add_drink("Tea","White-yellowish tea",60,"YellowSnows")
# print(bakery.drinks_menu)
sep("ädd table")
print(bakery.add_table("InsideTable",1,511))
# bakery.add_table("InsideTable",1,511)
print(bakery.add_table("InsideTable",11,5))
print(bakery.add_table("OutsideTable",100,800))
print(bakery.add_table("OutsideTable",51,12))
# print(bakery.add_table("OutsideTable",51,511))
print(bakery.get_free_tables_info())
sep("reserve table")
print(bakery.reserve_table(511))
print(bakery.reserve_table(510))
print(bakery.reserve_table(3))
print(bakery.reserve_table(5))
sep("order food")
print(bakery.order_food(1,"Milk dropperies","Chickopagos","Magullos","Calambores"))
print(bakery.order_food(100,"Silk dropperies","Chickopagos","Magullos","Calambores"))
print(bakery.order_food(100,"Homemade bread","Extraordinary cake","Regular cake","Calambores"))
sep("order drinks")
print(bakery.order_drink(11,"Snowy waters","White-yellowish tea","Muse tea","Tensive tea","Awesome tea"))
sep("leave table")
print(bakery.leave_table(1))
print(bakery.leave_table(11))
print(bakery.reserve_table(3))
print(bakery.reserve_table(5))
sep("get free tables info")
print(bakery.get_free_tables_info())
sep("total income")
print(bakery.get_total_income())



