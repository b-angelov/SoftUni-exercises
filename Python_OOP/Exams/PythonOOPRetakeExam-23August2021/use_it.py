from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.space_station import SpaceStation
from project.common_functions import *

class temp:

    def __init__(self,these_things,name,spec = 120):
        self.name = name
        self.things = these_things.split()
        self.spec = spec

thing = temp("a b cet ref gr","tng")
mings = temp("led wet fge","mng",11)
wings = temp("sop lob bob","wng",221)
bings = temp("ding dring wring","bng",-221)
things = [thing,mings,wings]
add_to_collection_or_error(bings,things,"name",bings.name,"Mess")

th = get_from_collection_or_error(things,"spec",11,"gng not here",op=">",whole=True)
print(th)
print(remove_from_collection_or_error(things,"name","wng","gng not here"))
print(things)

sep("my tests",symbols=50)
sep("astronaut")
amy = Biologist("Amy Farahfowler")
sheldon = Geodesist("Sheldon Cooper")
leonard = Meteorologist("Leonard Hopfstether")
raj = Meteorologist("Rajesh Coudrapally")
print(amy.condition(),leonard.condition(),sheldon.condition(),sep="\n")
sep("astronaut repository")
astronaut_repo = AstronautRepository()
astronaut_repo.add(raj)
astronaut_repo.add(leonard)
astronaut_repo.add(amy)
print(astronaut_repo.astronauts)
new_raj = astronaut_repo.find_by_name("Rajesh Coudrapally")
print(new_raj.condition())
astronaut_repo.remove(new_raj)
print(astronaut_repo.astronauts)
sep("planet")
earth = Planet("Earth")
moon = Planet("Moon")
venus = Planet("Venus")
sep("planet repository")
planet_repo = PlanetRepository()
planet_repo.add(earth)
planet_repo.add(moon)
planet_repo.add(venus)
print(planet_repo.planets)
planet_repo.remove(moon)
planet_found = planet_repo.find_by_name("Venus")
print(planet_found.items)
sep("space_station",symbols=30)
sep("add astronaut")
station = SpaceStation()
print(station.add_astronaut("Biologist","Amy Farahfowler"))
print(station.add_astronaut("Geodesist","Sheldon Cooper"))
print(station.add_astronaut("Meteorologist","Leonard Hopfstether"))
print(station.add_astronaut("Meteorologist","Rajesh Coudrapally"))
print(station.add_astronaut("Biologist","Amy Farahfowler"))
sep("add planet")
print(station.add_planet("Earth","cuprum, potassium, microscopic items, earthenwear" + (", mud" * 9)))
print(station.add_planet("Earth","cuprum, potassium, microscopic items, earthenwear"))
print(station.add_planet("Moon","rocks, schists, sediments, dust"))
print(station.add_planet("Venus","hot things, cool things, useless things, some things"))
sep("retire astronaut")
print(station.retire_astronaut("Rajesh Coudrapally"))
print(station.add_astronaut("Meteorologist","Rajesh Coudrapally"))
print(station.astronaut_repository.find_by_name("Sheldon Cooper"))
sep("recharge oxygen")
print(station.astronaut_repository.astronauts[0].condition())
print(station.recharge_oxygen())
print(station.astronaut_repository.astronauts[0].condition())
sep("send on mission")
# station.astronaut_repository.astronauts.clear()
print(station.report())
print(station.send_on_mission("Earth"))
print(station.send_on_mission("Venus"))
sep("report")
print(station.report())

zip_current_project()



