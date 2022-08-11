from project.drink.drink import Drink


class Tea(Drink):

    TEA_COST = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.TEA_COST, brand)