from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):

    __INITIAL_CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.__class__.__INITIAL_CAPACITY)