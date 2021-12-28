from project1.appliances.fridge import Fridge
from project1.appliances import Stove
from project1.appliances import TV
from project1.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        