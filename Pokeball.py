

class PokeBall:
    def __init__(self , ball_type):
        self.ball_type = ball_type
        self.catch_rate = None

    def get_catch_rate(self):
        return self.catch_rate

    def set_catch_rate(self, rate):
        self.catch_rate = rate

    def get_ball_type(self):
        return self.ball_type

    def catch(self , pokemon_health):
        if (pokemon_health):# Some logic that will avoid it catching the pokemon without fight
            return False
        return False



class GreatBall (PokeBall) :
    def __init__(self):
        super().__init__("Great Ball")
        self.set_catch_rate(0.5)


class UltraBall (PokeBall) :
    def __init__(self):
        super().__init__("Ultra Ball")
