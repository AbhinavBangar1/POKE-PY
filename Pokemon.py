

class Pokemon :
    def __init__(self,name,element_type):
        self.__nickname = None
        self.name = name
        self.element_type = element_type
        self.__health = 100
        self.__level = 1
        self.__speed = 25
        self.__stamina = 30
        self.__experience = 0

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)

    def evolve(self , name):
        self.__level = 1
        self.health += self.health * 0.3
        self.name = name
        self.__speed += self.__speed * 0.1
        self.__stamina += self.__stamina * 0.2

    def take_damage(self , amount):
        self.health -= amount

    def has_fainted(self):
        return self.health <= 0

    def get_stamina(self):
        return self.__stamina

    def gain_exp(self , exp):
        self.__experience +=exp

    def upgrade(self):
        self.__level += 1

    def set_nickname(self , nickname):
        self.__nickname = nickname




# class common(Pokemon) :
