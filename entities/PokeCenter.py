
## Assumption here : one city will have only one pokemon center
class PokeCenter:
    PokemonCenters = {} # City : coordinates
    def __init__ (self , nurse , helper , coordinates , city):
        self.nurse = nurse
        self.helper = helper
        self.coordinates = coordinates
        self.city = city
        PokeCenter.PokemonCenters[city] = self

    # def get_nearest_centre(self , c_coordinates , t_coordinates):
    def heal (self , pokemon) :
        treatment = pokemon.max_health - pokemon.health

