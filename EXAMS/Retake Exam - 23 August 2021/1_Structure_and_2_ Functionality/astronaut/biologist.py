from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    BREATH_UNITS = 5
    INITIAL_UNITS = 70

    def __init__(self, name):
        super().__init__(name, self.INITIAL_UNITS)
