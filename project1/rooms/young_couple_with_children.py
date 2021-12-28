from project1.appliances.fridge import Fridge
from project1.appliances import Laptop
from project1.appliances import TV
from project1.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one+salary_two, 2 + len(children))
        self.room_cost = 30
        self.appliances = [[TV()]* self.members_count, [Fridge()]* self.members_count, [Laptop()]* self.members_count]
        self.children = [children]