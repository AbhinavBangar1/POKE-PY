
from Pokedex import Pokedex
from Pokeball import PokeBall

class Trainer :
    def __init__(self, name, experience, city , coordinates ):
        self.__experience = experience
        self.name = name
        self.__badges  = []
        self.__pokemons  = [] ## list of pokemon object
        self.__city = city
        self.coordinates = coordinates
        self.__backpack = []
        self.__pokeballs = {}
        self.__backpack_capacity = 10
        self.pokedex = Pokedex()

    def catch_pokemon(self , pokeball , pokemon): ## assuming the check if pokeball exists will be done in pygame interface
        self.__pokeballs[pokeball] -= 1
        if pokeball.catch() :
            self.__pokemons.append(pokemon)


    def upgrade_back_capacity(self):
        self.__backpack_capacity += 1

    def added_to_backpack(self, item):
        if len(self.__backpack) > self.__backpack_capacity:
            self.__backpack.append(item)
            return True
        else :
            return False

    def removed_from_backpack(self , item):
        if len(self.__backpack) > 0 :
            self.__backpack.remove(item)
            return True
        else :
            return False