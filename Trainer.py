import keyboard
from Pokedex import Pokedex

class Trainer :
    def __init__(self, name, experience, city , coordinates ):
        self.experience = experience
        self.name = name
        self.badges  = []
        self.pokemons  = []
        self.city = city
        self.coordinates = coordinates
        self.backpack = []
        self.pokeball = 3
        self.backpack_capacity = 10
        self.pokedex = Pokedex()

    def upgrade_back_capacity(self):
        self.backpack_capacity += 1

    def added_to_backpack(self, item):
        if len(self.backpack) > self.backpack_capacity:
            self.backpack.append(item)
            return True
        else :
            return False

    def removed_from_backpack(self , item):
        if len(self.backpack) > 0 :
            self.backpack.remove(item)
            return True
        else :
            return False

    def move(self):
        key = keyboard.read_key()
        if key == "w" :
            self.coordinates[1] += 1
        if key == "a":
            self.coordinates[0] -= 1
        if key == "s":
            self.coordinates[1] -= 1
        if key == "d":
            self.coordinates[0] += 1





