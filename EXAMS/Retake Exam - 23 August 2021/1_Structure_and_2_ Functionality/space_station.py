from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository

class Objects:

    @staticmethod
    def create_astronaut(astronaut_type, name):
        if astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            return Meteorologist(name)


class SpaceStation:

    def __init__(self):
        self.missions = {'successful': 0, 'failed': 0}
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type in ("Biologist", "Geodesist", "Meteorologist"):
            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."
            new_astronaut = Objects.create_astronaut(astronaut_type, name)
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet.from_name_items(name, items)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        found_astronaut = self.astronaut_repository.find_by_name(name)
        if found_astronaut:
            self.astronaut_repository.remove(found_astronaut)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        selected_planet = self.planet_repository.find_by_name(planet_name)
        if selected_planet:
            astronauts = deque(self.astronaut_repository.find_top_five('oxygen'))
            if len(astronauts) > 0:
                items = selected_planet.items
                sent_to_explore = 0
                while astronauts and items:
                    astronaut = astronauts.popleft()
                    sent_to_explore += 1
                    while astronaut.breaths_left > 0 and items:
                        item = items.pop()
                        astronaut.get_item(item)

                if items:
                    self.missions['failed'] += 1
                    return "Mission is not completed."

                self.missions['successful'] += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{sent_to_explore} astronauts participated in collecting items."

            raise Exception("You need at least one astronaut to explore the planet!")
        raise Exception("Invalid planet name!")

    def report(self):
        result = f"{self.missions.get('successful', 0)} successful missions!" \
                 f"\n{self.missions.get('failed', 0)} missions were not completed!" \
                 f"\nAstronauts' info:"
        result += '\n' + '\n'.join([astronaut.info for astronaut in self.astronaut_repository.astronauts])
        return result.rstrip()
