from project.horse_race_app import HorseRaceApp

horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))


######MY TESTS#################

# horse_race_app
print(horseRaceApp.add_horse("Appaloosa", "Horsie", 120))
print(horseRaceApp.add_horse("Thoroughbred", "Horsefold", 140))
print(horseRaceApp.add_horse("Thoroughbred", "Puh Bear", 81))
print(horseRaceApp.add_jockey("Christopher Robin", 18))
print(horseRaceApp.add_jockey("Robin Hood", 18))
print(horseRaceApp.create_horse_race("Winter"))
# print(horseRaceApp.create_horse_race("Winter"))
for _ in range(20):
    horseRaceApp.horses[-1].train()
print(horseRaceApp.add_horse_to_jockey("Christopher Robin","Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Christopher Robin","Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Robin Hood","Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Winter","Christopher Robin"))
print(horseRaceApp.add_jockey_to_horse_race("Winter","Robin Hood"))
print(horseRaceApp.start_horse_race("Winter"))