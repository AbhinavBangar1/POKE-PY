


class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.pokemon1 = None
        self.pokemon2 = None

    def choose_pokemon(self, trainer, pokemon):
        if trainer == self.trainer1:
            self.pokemon1 = pokemon
        elif trainer == self.trainer2:
            self.pokemon2 = pokemon

    def change_pokemon(self, trainer, pokemon):
        if trainer == self.trainer1:
            self.pokemon1 = pokemon
        elif trainer == self.trainer2:
            self.pokemon2 = pokemon
