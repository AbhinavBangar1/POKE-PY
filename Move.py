import random

class Move :
    def __init__ (self , name = None , damage = None , move_type = None, accuracy = None , stamina_cost = None):
        self.name = name
        self.damage = damage
        self.move_type = move_type
        self.accuracy = accuracy
        self.stamina_cost = stamina_cost

    def use(self, pokemon1 , pokemon2):
        if pokemon1.stamina >= self.stamina_cost :
            if self.check_hit() :
                pokemon2.take_damage(self.damage)
            pokemon1.stamina -= self.stamina_cost

    def check_hit(self):
        return random.randint(1, 100) <= self.accuracy

class SpecialMove(Move) :
    def __init__(self):
        super().__init__()



