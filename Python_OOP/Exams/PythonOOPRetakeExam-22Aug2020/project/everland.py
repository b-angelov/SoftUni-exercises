from project.rooms.room import Room

class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = sum(room.expenses + room.room_cost for room in self.rooms)
        return f"Monthly consumption: {consumption:.2f}$."

    def pay(self):
        out = []
        removable = []
        for room in self.rooms:
            expenses = room.expenses + room.room_cost
            if expenses <= room.budget:
                room.budget -= expenses
                out.append(f"{room.family_name} paid {expenses:.2f}$ and have {room.budget:.2f}$ left." )
            else:
                out.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                removable.append(room)
        set(map(self.rooms.remove,removable))
        return "\n".join(out)

    def status(self):
        total_population = sum(room.members_count for room in self.rooms)
        room_head = "{} with {} members. Budget: {:.2f}$, Expenses: {:.2f}$"
        child_info = "--- Child {} monthly cost: {:.2f}$"
        appliance_info = "--- Appliances monthly cost: {:.2f}$"
        out = [f"Total population: {total_population}"]
        for room in self.rooms:
            out.append(room_head.format(room.family_name,room.members_count,room.budget,room.expenses))
            if room.children:
                for n,child in enumerate(room.children):
                    out.append(child_info.format(n+1,child.cost * 30))
            if room.appliances:
                out.append(appliance_info.format(sum(appliance.get_monthly_expense() for appliance in room.appliances)))
        return "\n".join(out)
