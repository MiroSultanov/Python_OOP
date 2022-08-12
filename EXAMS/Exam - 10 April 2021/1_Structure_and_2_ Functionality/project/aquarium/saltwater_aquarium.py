from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):

    __INITIAL_CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, self.__class__.__INITIAL_CAPACITY)