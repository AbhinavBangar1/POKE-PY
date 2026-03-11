import random

class Move :
    def __init__ (self , name , damage , move_type , accuracy , stamina_cost):
        self.name = name
        self.damage = damage
        self.move_type = move_type
        self.accuracy = accuracy
        self.stamina_cost = stamina_cost
        self.effect = None

    def use(self, pokemon1 , pokemon2):
        if pokemon1.stamina >= self.stamina_cost and self.check_hit():
            pokemon2.take_damage(self.damage)
            pokemon1.stamina -= self.stamina_cost

    def check_hit(self):
        return random.randint(1, 100) <= self.accuracy


