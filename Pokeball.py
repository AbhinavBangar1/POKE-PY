import random

class PokeBall:

    def __init__(self , ball_type):
        self.ball_type = ball_type
        self.catch_rate = 0.1

    def get_catch_rate(self):
        return self.catch_rate

    def set_catch_rate(self, rate):
        self.catch_rate = rate

    def get_ball_type(self):
        return self.ball_type

    def catch(self, pokemon):
        health_factor = 1 - (pokemon.health / pokemon.max_health)
        final_chance = self.catch_rate + 0.5 * health_factor
        roll = random.random()
        if roll <= final_chance:
            return True
        else:
            print(f"Oh no! {pokemon.name} broke free.")
            return False

    def craft_pokeball(apricorn = None):
        ball_map = {
            'white_apricorn': 'GreatBall'
        }
        ball = ball_map[apricorn]
        if ball == 'GreatBall':
            GreatBall()



class GreatBall (PokeBall) :
    def __init__(self):
        super().__init__("Great Ball")
        self.set_catch_rate(0.5)


class UltraBall (PokeBall) :
    def __init__(self):
        super().__init__("Ultra Ball")
        self.set_catch_rate(0.7)

class MasterBall(PokeBall) :
    def __init__(self):
        super().__init__("Master Ball")
        self.set_catch_rate(0.9)



