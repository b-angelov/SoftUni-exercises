from project.supply.supply import exc
# from supply.supply import exc
# from supply.drink import Drink
# from supply.food import Food
from project.supply.supply import Supply
# from supply.supply import Supply
from project.player import Player
# from player import Player

def check_lists(function):
    def check(**kwargs):
        condition = kwargs.get("error_raise_condition",True)
        no_error = kwargs.get("do_not_raise_error", False)
        name = kwargs.get("name",True)
        attr1 = kwargs.get("attr1",name)
        name1 = kwargs.get("name1",name)
        att = kwargs.get("attr",name)
        excp = kwargs.get("exc",Exception)
        ob = [value for value in kwargs["collection"] if function(getattr(value, att, name),name) and function(getattr(value,attr1,name1),name1)]
        if condition:
            condition = bool(ob)
        else:
            condition = bool(not ob)
        if not no_error:
            exc(kwargs.get("error_message", ""),condition,excp)
        return ob[kwargs.get("item",0)] if ob else False
    return check

@check_lists
def check_collections(cond, val, op ="=="):
    if op == "==":
        return cond == val
    if op == "!=":
        return cond != val

class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        tmp_playlist = []
        for player in sorted(set(players),key=players.index):
            if player not in self.players:
                tmp_playlist.append(player)
        self.players += tmp_playlist
        return f"Successfully added: {', '.join(player.name for player in tmp_playlist)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player: Player = check_collections(
            collection=self.players,
            attr="name", name=player_name,
            do_not_raise_error=True,error_raise_condition=False
        )
        if not player:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        if sustenance_type not in ["Food","Drink"]:
            return
        miss = "There are no drink supplies left!"
        if sustenance_type == "Food":
            miss = "There are no food supplies left!"
        supply: Supply  = check_collections(
                collection=self.supplies,
                attr="supply_name", name=sustenance_type, item=-1,
                error_raise_condition=False,error_message=miss
            )
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        self.supplies.reverse()
        self.supplies.remove(supply)
        self.supplies.reverse()
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        winner = None
        first_player = check_collections(
            collection=self.players,
            attr="name", name=first_player_name,
            do_not_raise_error=True
        )
        second_player = check_collections(
            collection=self.players,
            attr="name", name=second_player_name,
            do_not_raise_error=True
        )
        stamina_check = [player for player in (first_player,second_player) if player.stamina == 0]
        if any(stamina_check):
            return "\n".join(f"Player {player.name} does not have enough stamina." for player in stamina_check)
        begin = sorted([first_player,second_player], key=lambda player: player.stamina)
        try:
            begin[-1].stamina -= begin[0].stamina / 2
        except:
            begin[-1].stamina = 0
            winner = begin[0]
        if not winner:
            try:
                begin[0].stamina -= begin[-1].stamina / 2
            except:
                begin[0].stamina = 0
                winner = begin[-1]
            if not winner:
                winner = max(begin, key=lambda player: player.stamina)
        return f"Winner: {winner.name}"

    def next_day(self):
        def dec(player):
            try:
                player.stamina -= player.age * 2
            except:
                player.stamina = 0
        set(map(dec, self.players))
        fully_sustain = lambda player: (self.sustain(player.name,"Food"),self.sustain(player.name,"Drink"))
        list(map(fully_sustain,self.players))
        # set(map(lambda player: self.sustain(player.name, "Food"),self.players))
        # set(map(lambda player: self.sustain(player.name, "Drink"),self.players))

    def __str__(self):
        a = [str(player) for player in self.players]
        a.extend(supply.details() for supply in self.supplies)
        return "\n".join(a)