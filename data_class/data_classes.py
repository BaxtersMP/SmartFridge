from data_class.sql_text_input import *
from db_lookup.perishable_lookup import *


class Food:
    pass


class Perishable:
    def __init__(self, name, weight, perishable_type, location, storage, age=None):
        if age is None:
            age = 0
        self.name = name
        self.initial_weight = weight
        self.current_weight = weight
        self.perishable_type = perishable_type
        self.age = age
        self.location = location
        self.storage = storage
        self.lifespan = get_perishable_lifespan(self.perishable_type)

    def get_status(self):
        if self.age < self.lifespan:
            return FoodStatus.Good
        else:
            return FoodStatus.Spoiled

    def get_lifespan(self):
        return get_perishable_lifespan(self.perishable_type)

weight1 = Perishable()
