## a entry will have a list [pokemon name , seen , caught]

class Pokedex:
    def __init__(self):
        self.__entries = {}

    def addPoketoDex(self , pokemom): # Helper function
        self.__entries[pokemon] = [pokemon , 1 , 0]

    def checkPokedex(self , pokemon): # check in pokedex if that pokemon is seen before
        if pokemon in self.__entries:
            return self.__entries[pokemon]
        else :
            return False

    def updatePokedex(self , pokemon):
        if pokemon in self.__entries:
            self.__entries[pokemon][2] = 1 # player catch the pokemon
        else :
            self.addPoketoDex(pokemon)

    ## Completed