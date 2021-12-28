from project1.appliances.fridge import Fridge
from project1.appliances import Laptop
from project1.appliances import TV
from project1.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one, salary_two):
        super().__init__(family_name, salary_one+salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]