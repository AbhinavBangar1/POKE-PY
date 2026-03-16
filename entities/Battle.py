import random


class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.pokemon1 = None
        self.pokemon2 = None
        self.current_trainer = random.choice([self.trainer1, self.trainer2])

    def choose_pokemon(self, trainer):
        for p in trainer.pokemons:
            if not p.has_fainted():
                pokemon = p
                break
        if trainer == self.trainer1:
            self.pokemon1 = pokemon
        elif trainer == self.trainer2:
            self.pokemon2 = pokemon

    def change_pokemon(self, trainer , new_pokemon): ## handle the new pokemon thing in game logic
        if trainer == self.trainer1 and new_pokemon != self.pokemon1 and not new_pokemon.has_fainted():
            self.pokemon1 = new_pokemon
        elif trainer == self.trainer2 and new_pokemon != self.pokemon2 and not new_pokemon.has_fainted():
            self.pokemon2 = new_pokemon

    def winner(self):
        if self.pokemon1.has_fainted() :
            self.pokemon1.is_available = False
            return  self.trainer2
        elif self.pokemon2.has_fainted() :
          return self.trainer1
        else :
            return "Continue"



    def attack(self, move):
        current_trainer = self.current_trainer
        if current_trainer == self.trainer1:
            attacker = self.pokemon1
            defender = self.pokemon2
        else:
            attacker = self.pokemon2
            defender = self.pokemon1
        move.use(attacker, defender)

        self.current_trainer = (self.trainer2 if current_trainer == self.trainer1 else self.trainer1)
        return self.winner()

# Completed