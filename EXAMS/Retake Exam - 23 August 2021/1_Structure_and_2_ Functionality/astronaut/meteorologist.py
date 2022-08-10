from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    BREATH_UNITS = 15
    INITIAL_UNITS = 90

    def __init__(self, name):
        super().__init__(name, self.INITIAL_UNITS)