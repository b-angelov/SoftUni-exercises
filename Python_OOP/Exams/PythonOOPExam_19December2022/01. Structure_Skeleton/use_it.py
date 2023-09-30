from project.concert_tracker_app import ConcertTrackerApp

musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))


##########MY TESTS############################
# app.remove_musician_from_band("Alex","RockName")
print(*list(member.name for member in app.bands[0].members))
names = ["Клапти","Доброч","Патапан"]
for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))
print(app.create_musician("Singer", "Беломир Кападокийски", 20))

print(app.create_band("ПАтаПАнциТЕ"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "ПАтаПАнциТЕ"))
print(app.create_concert("Metal", 815, 22.20, 877.7, "Varna"))
print(app.musicians[3].learn_new_skill("sing low pitch notes"))
print(app.musicians[4].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[5].learn_new_skill("play metal"))
print(app.start_concert("Varna", "ПАтаПАнциТЕ"))
print(app.musicians[4].learn_new_skill("play the drums with drum brushes"))
print(app.musicians[3].learn_new_skill("sing high pitch notes"))
print(app.musicians[5].learn_new_skill("play jazz"))
print(app.create_concert("Jazz", 20874, 55514.20, 566255.7, "Obzor"))
print(app.start_concert("Obzor", "ПАтаПАнциТЕ"))
print(list(map(lambda a: a.__class__.__name__, app.bands[1].members)))

# print(app.add_musician_to_band("Беломир Кападокийски", "Цапцаруфляците"))
# print(app.add_musician_to_band("Беломир К", "ПАтаПАнциТЕ"))

#concert_tracker_app

print(app.create_musician("Drummer","Slavi",16))
# print(app.create_musician("Drummer","Slavi",16))

print(app.create_band("Розоберас")) #! space symbol band allowed
# print(app.create_band("Розоберас"))

print(app.create_concert("Metal",184,1.12,8411,"Astoria hall"))
# print(app.create_concert("Metal",184,1.12,8411,"Astoria hall"))

