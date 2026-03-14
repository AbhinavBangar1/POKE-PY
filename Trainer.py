import math

from Pokedex import Pokedex
from Pokeball import PokeBall
from PokeCenter import PokeCenter


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

    @property
    def experience(self):
        return self.__experience

    def gain_experience(self, experience):
        self.__experience += experience

    @property
    def city(self):
        return self.__city

    @property
    def pokemons(self):
        return self.__pokemons

    @property
    def badges(self):
        return self.__badges

    def add_badge(self, badge):
        self.__badges.append(badge)

    @property
    def pokeballs(self):
        return self.__pokeballs

    @property
    def backpack(self):
        return self.__backpack


    def choose_move(self , pokemon):## assuming this will be used in game interface when user selects the move from interface
        m = input()
        return pokemon.moves[int(m)]


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

    def get_nearest_centre(self):
        t_x , t_y = self.coordinates[0] , self.coordinates[1]
        mindist = float('inf')
        for pokecenter in PokeCenter.PokemonCenters:
            p_x , p_y = pokecenter.coordinates[0] , pokecenter.coordinates[1]
            dist = math.sqrt( (p_x - t_x)**2 + (p_y - t_y)**2 )
            if dist < mindist :
                mindist = dist
                nearest_center = pokecenter
        return nearest_center
