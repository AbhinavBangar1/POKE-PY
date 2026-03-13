

class Pokemon :
    def __init__(self, health , stamina , speed , max_health ,element_type = None ,name = None):
        self.__nickname = None
        self.name = name
        self.__element_type = element_type
        self.__health = health
        self.max_health = max_health
        self.__level = 1
        self.__speed = speed
        self.__stamina = stamina
        self.__experience = 0
        self.__moves = []
        self.__rarity = "common"

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)

    def take_damage(self , amount):
        self.health -= amount

    def has_fainted(self):
        return self.health <= 0

    @property
    def element_type(self):
        return self.__element_type

    @property
    def level(self):
        return self.__level

    def upgrade(self):
        self.__level += 1

    @property
    def speed(self):
        return self.__speed

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__stamina = value

    def feed(self , quantity_food):
        self.__stamina += quantity_food

    @property
    def moves(self):
        return self.__moves

    def add_move(self , move ):
        self.__moves.append(move)

    def can_add (self) :
        if len(self.__moves) > 5 : # can add 6 pokemon
            return False
        return True

    @property
    def experience(self):
        return self.__experience

    def gain_exp(self , exp):
        self.__experience +=exp

    @property
    def rarity(self):
        return self.__rarity
    @rarity.setter
    def rarity(self, rare):
        self.__rarity = rare

    def evolve(self , name):
        self.__level += 1
        self.health += self.health * 0.3
        self.name = name
        self.__speed += self.__speed * 0.1
        self.__stamina += self.__stamina * 0.2

    def set_nickname(self , nickname):
        self.__nickname = nickname


class Common(Pokemon) :
    def __init__(self):
        super().__init__(health= 100 , stamina= 25 , speed = 5)
        rarity = "common"

class Rare(Pokemon) :
    def __init__(self):
        super().__init__(health= 120 , stamina= 30 , speed = 6)
        rarity = "rare"

class Epic(Pokemon) :
    def __init__(self):
        super().__init__(health= 140 , stamina= 40 , speed = 7)
        rarity = "Epic"

class Legendary(Pokemon) :
    def __init__(self):
        super().__init__(health= 160 , stamina= 45 , speed = 15)
        rarity = "legendary"

class Mythic(Pokemon) :
    def __init__(self):
        super().__init__(health= 200 , stamina= 55 , speed = 20)
        rarity = "Mythic"

## Completed