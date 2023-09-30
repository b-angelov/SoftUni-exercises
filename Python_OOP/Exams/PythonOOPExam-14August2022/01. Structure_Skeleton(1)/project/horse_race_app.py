from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace
# from horse_specification.appaloosa import Appaloosa
# from horse_specification.thoroughbred import Thoroughbred
# from jockey import Jockey
# from horse_race import HorseRace

class HorseRaceApp:

    HORSE_TYPES = {"Appaloosa":Appaloosa,"Thoroughbred":Thoroughbred}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        self.__is_horse_already_added(horse_name)
        if horse_type in self.HORSE_TYPES.keys():
            self.horses.append(self.HORSE_TYPES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        self.__is_jockey_already_added(jockey_name)
        self.jockeys.append(Jockey(jockey_name,age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        self.__is_race_already_added(race_type)
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__get_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.__are_horse_type_horses_available(horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.rider = jockey
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__get_race_by_name(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__get_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        elif not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if self.__get_jockey_in_races(jockey_name):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        race = self.__get_race_by_name(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = self.__get_winner(race_type)
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."


    def __get_horse_by_name(self, name: str):
        horse = [horse for horse in self.horses if horse.name == name]
        if horse: return horse[0]

    def __get_horse_by_type(self, type: str, is_taken = False):
        horse = [horse for horse in self.horses if horse.__class__.__name__ == type and horse.is_taken == is_taken]
        if horse: return horse[-1]

    def __get_jockey_by_name(self, name: str):
            jockey = [jockey for jockey in self.jockeys if jockey.name == name]
            if jockey: return jockey[0]

    def __get_race_by_name(self, name: str):
            horse_race = [horse_race for horse_race in self.horse_races if horse_race.race_type == name]
            if horse_race: return horse_race[0]

    def __is_horse_already_added(self, horse: str):
        horse = self.__get_horse_by_name(horse)
        if horse:
            raise Exception(f"Horse {horse.name} has been already added!")

    def __is_jockey_already_added(self, jockey: str):
        jockey = self.__get_jockey_by_name(jockey)
        if jockey:
            raise Exception(f"Jockey {jockey.name} has been already added!")

    def __is_race_already_added(self, race: str):
        race = self.__get_race_by_name(race)
        if race:
            raise Exception(f"Race {race.race_type} has been already created!")

    def __are_horse_type_horses_available(self, horse_type):
        horse = self. __get_horse_by_type(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        return horse

    def __get_jockey_in_races(self, name):
        return any(jockey.name == name for race in self.horse_races for jockey in race.jockeys)

    def __get_winner(self, race_type):
        race = self.__get_race_by_name(race_type)
        return max((jockey for jockey in race.jockeys), key=lambda jockey: jockey.horse.speed)


