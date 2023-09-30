from project.room import Room

class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def from_stars(stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self,room_number: int, people: int):
        room = [room for room in self.rooms if room.number == room_number]
        if room and not room[0].is_taken:
            room = room[0]
            room.take_room(people)
            if room.is_taken:
                self.guests += room.guests


    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number]
        if room:
            room = room[0]
            guests = room.guests
            room.free_room()
            self.guests -= guests

    def status(self):
        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {", ".join(str(room.number) for room in self.rooms if not room.is_taken)}
Taken rooms: {", ".join(str(room.number) for room in self.rooms if room.is_taken)}"""

