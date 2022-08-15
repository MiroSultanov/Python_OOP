from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseFactory:
    valid_horse_types = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    @staticmethod
    def create_horse(horse_type: str, horse_name: str, horse_speed: int):
        return HorseFactory.valid_horse_types[horse_type](horse_name, horse_speed)


class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_is_less_than_min_symbols(name, min_symbols, message):
        if len(name) < min_symbols:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_bigger_than_max_value(value, max_value, message):
        if value > max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_race_type_not_valid(race_type, message):
        valid_race_types = ["Winter", "Spring", "Autumn", "Summer"]
        if race_type not in valid_race_types:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_already_exists_in_collection(collection, name, message):
        if any([obj.name == name for obj in collection]):
            raise Exception(message)

    @staticmethod
    def raise_if_race_type_already_exists(collection, race_type, message):
        if any([obj.race_type == race_type for obj in collection]):
            raise Exception(message)

    @staticmethod
    def find_available_jockey_raise_if_none(jockeys, name, message):
        for j in jockeys:
            if j.name == name:
                return j
        raise Exception(message)

    @staticmethod
    def find_available_horse_raise_if_none(horses, horse_type, message):
        for idx in range(len(horses) - 1, -1, -1):
            horse = horses[idx]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(message)

    @staticmethod
    def find_available_race_raise_if_none(races, race_type, message):
        for race in races:
            if race.race_type == race_type:
                return race
        raise Exception(message)

    @staticmethod
    def raise_if_jockey_doesnt_have_a_horse(jockey, message):
        if jockey.horse is None:
            raise Exception(message)

    @staticmethod
    def raise_if_not_enough_jockeys_in_race(race, message):
        if len(race.jockeys) < 2:
            raise Exception(message)


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horse_types = ["Appaloosa", "Thoroughbred"]
        if horse_type in valid_horse_types:
            Validator.raise_if_name_already_exists_in_collection(
                self.horses,
                horse_name,
                f"Horse {horse_name} has been already added!"
            )
            horse = HorseFactory.create_horse(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        Validator.raise_if_name_already_exists_in_collection(
            self.jockeys,
            jockey_name,
            f"Jockey {jockey_name} has been already added!"
        )
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        Validator.raise_if_race_type_already_exists(
            self.horse_races,
            race_type,
            f"Race {race_type} has been already created!"
        )
        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = Validator.find_available_jockey_raise_if_none(
            self.jockeys,
            jockey_name,
            f"Jockey {jockey_name} could not be found!"
        )

        horse = Validator.find_available_horse_raise_if_none(
            self.horses,
            horse_type,
            f"Horse breed {horse_type} could not be found!"
        )
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = Validator.find_available_race_raise_if_none(
            self.horse_races,
            race_type,
            f"Race {race_type} could not be found!"
        )
        jockey = Validator.find_available_jockey_raise_if_none(
            self.jockeys,
            jockey_name,
            f"Jockey {jockey_name} could not be found!"
        )
        Validator.raise_if_jockey_doesnt_have_a_horse(jockey, f"Jockey {jockey_name} cannot race without a horse!")

        if any([j.name == jockey_name for j in race.jockeys]):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = Validator.find_available_race_raise_if_none(
            self.horse_races,
            race_type,
            f"Race {race_type} could not be found!"
        )
        Validator.raise_if_not_enough_jockeys_in_race(race, f"Horse race {race_type} needs at least two participants!")

        racers = list(sorted(race.jockeys, key=lambda x: -x.horse.speed))
        winner = racers[0]

        return f"The winner of the {race_type} race," \
               f" with a speed of {winner.horse.speed}km/h is {winner.name}!" \
               f" Winner's horse: {winner.horse.name}."