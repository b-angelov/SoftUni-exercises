from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:

    type_references = {"Singer":Singer, "Drummer":Drummer, "Guitarist":Guitarist}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.type_references.keys():
            raise ValueError("Invalid musician type!")
        if name in (m.name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")
        self.musicians.append(self.type_references[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in (b.name for b in self.bands):
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self,genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in (c.place for c in self.concerts):
            concert_genre = [c.genre for c in self.concerts if c.place == place][0]
            raise Exception(f"{place} is already registered for {concert_genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price,expenses,place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self,musician_name: str, band_name: str):
        if musician_name not in (m.name for m in self.musicians):
            raise Exception(f"{musician_name} isn't a musician!")
        if band_name not in (b.name for b in self.bands):
            raise Exception(f"{band_name} isn't a band!")
        band = [b for b  in self.bands if b.name == band_name][0]
        musician = [m for m  in self.musicians if m.name == musician_name][0]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in (b.name for b in self.bands):
            raise Exception(f"{band_name} isn't a band!")
        band = [b for b  in self.bands if b.name == band_name][0]
        if musician_name not in (m.name for m in band.members):
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = [m for m in band.members if m.name == musician_name][0]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."


    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        if not all(any(musician == member.__class__.__name__ for member in band.members) for musician in self.type_references.keys()):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        concert = [concert for concert in self.concerts if concert.place == concert_place][0]
        if concert.genre == "Rock":
            if not all(any(skill in member.skills for skill in ["play the drums with drumsticks","sing high pitch notes","play rock"]) for member in band.members):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            if not all(any(skill in member.skills for skill in ["play the drums with drumsticks","sing low pitch notes","play metal"]) for member in band.members):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            for member in band.members:
                if "play the drums with drum brushes" in member.skills:
                    pass
                elif "sing high pitch notes" in member.skills and "sing low pitch notes" in member.skills:
                    pass
                elif "play jazz" in member.skills:
                    pass
                else:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
