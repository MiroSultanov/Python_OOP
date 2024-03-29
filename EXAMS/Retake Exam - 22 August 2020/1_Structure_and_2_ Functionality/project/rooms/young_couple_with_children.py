from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class YoungCoupleWithChildren(Room):

    _ROOM_COST = 30
    _APPLIANCES = [TV(), Fridge(), Laptop()]
    _MEMBERS_COUNT = 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children) -> None:
        members_count = self.__class__._MEMBERS_COUNT + len(children)
        super().__init__(family_name, salary_one + salary_two, members_count)
        self.room_cost = self.__class__._ROOM_COST
        self.appliances = self.__class__._APPLIANCES * self.members_count
        self.children.extend(children)
        self.calculate_expenses(self.appliances, self.children)