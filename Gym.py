import time

from Battle import Battle

class Gym :
    def __init__(self , leader , badge , gym_type , league , exp_req):
        self.leader = leader # a trainer object
        self.badge = badge
        self.gym_type = gym_type
        self.league = league
        self.exp_req = exp_req

    def Can_Challenge(self , trainer):
        if trainer.experience < self.exp_req :
            return False
        else :
            return True

    def fight(self, trainer):
        if not self.Can_Challenge(trainer):
            return None

        battle = Battle(trainer, self.leader)

        battle.choose_pokemon(trainer )
        battle.choose_pokemon(self.leader)

        winner = "Continue"
        while winner == "Continue":
            current_trainer = battle.current_trainer
            if current_trainer == trainer:
                move = battle.trainer1.choose_move(battle.pokemon1)
            else: # meaning gym leader (use the move with max damage) (upgrade it by using a combination of stamina cost damage and accuracy )
                move = battle.pokemon2.moves[0]
                for m in battle.pokemon2.moves:
                    if (m.damage / m.accuracy)  > (move.damage / move.accuracy) :
                        move = m


            winner = battle.attack(move)

        if winner == trainer:
            trainer.add_badge(self.badge)
        return winner