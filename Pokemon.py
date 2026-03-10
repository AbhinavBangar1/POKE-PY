

class Pokemon :
    def __init__(self,name,element_type,health,level,speed,stamina,experience):
        self.nickname = None
        self.name = name
        self.element_type = element_type
        self.health = health
        self.level = level
        self.speed = speed
        self.stamina = stamina
        self.experience = experience

    def evolve(self , name):
        self.level = 1
        self.health += self.health * 0.3
        self.name = name
        self.speed += self.speed * 0.1
        self.stamina += self.stamina * 0.2

    def take_damage(self , amount):
        self.health -= amount

    def has_fainted(self):
        return self.health <= 0

    def get_stamina(self):
        return self.stamina

    def gain_exp(self , exp):
        self.experience +=exp

    def upgrade(self):
        self.level += 1

    def set_nickname(self , nickname):
        self.nickname = nickname




# class common(Pokemon) :
