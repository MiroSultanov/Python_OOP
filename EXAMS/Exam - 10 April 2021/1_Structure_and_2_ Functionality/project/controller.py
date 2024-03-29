from project.decoration.decoration_repository import DecorationRepository


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type in ("FreshwaterAquarium", "SaltwaterAquarium"):
            new_aquarium = eval(f"{aquarium_type}('{aquarium_name}')")
            self.aquariums.append(new_aquarium)
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type in ("Ornament", "Plant"):
            eval_str = f"{decoration_type}()"
            new_decoration = eval(eval_str)
            self.decorations_repository.add(new_decoration)
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        found_aquarium = self.find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            found_decoration = self.decorations_repository.find_by_type(decoration_type)
            if found_decoration != 'None':
                found_aquarium.decorations.append(found_decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."
            return "There isn't a decoration of type {decoration_type}."


    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        found_aquarium = self.find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            if fish_type in ("FreshwaterAquarium", "SaltwaterAquarium"):
                new_fish = eval(f'{fish_type}("{fish_name}", "{fish_species}", {price})')
                if found_aquarium.aquarium_type != new_fish.allowed_habitat:
                    return f"Water not suitable."
                return found_aquarium.add_fish(new_fish)
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):
        found_aquarium = self.find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            found_aquarium.feed()
            return f"Fish fed: {len(found_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        found_aquarium = self.find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            result = found_aquarium.aquarium_value
            return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        result = '\n'.join([str(el) for el in self.aquariums])
        return result

    def find_aquarium_by_name(self, aquarium_name: str):
        if aquarium_name in [a.name for a in self.aquariums]:
            return next(el for el in self.aquariums if el.name == aquarium_name)
