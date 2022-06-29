from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        if pokemon_name in [p.name for p in self.pokemons]:
            for pokemon in self.pokemons:
                if pokemon.name == pokemon_name:
                    self.pokemons.remove(pokemon)
                    return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = f"Pokemon Trainer {self.name}\n"
        result += f'Pokemon count {len(self.pokemons)}'
        for pokemon in self.pokemons:
            result += '\n- ' + pokemon.pokemon_details()
        return result
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())



