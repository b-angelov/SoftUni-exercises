from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemon = [pokemon for pokemon in self.pokemons if pokemon.name == pokemon_name]
        if not pokemon:
            return "Pokemon is not caught"
        pokemon = self.pokemons.remove(pokemon[0])
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        res = '\n- '.join(pokemon.pokemon_details() for pokemon in self.pokemons)
        return f"""Pokemon Trainer {self.name}
Pokemon count {len(self.pokemons)}
- {res}"""


