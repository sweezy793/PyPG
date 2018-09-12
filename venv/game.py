import random

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Player:
    def __init__(self,health,mana,attack,defence,magic):
        self.maxhealth = health
        self.health = health
        self.maxmana = mana
        self.mana = mana
        self.maxattack = attack+10
        self.minattack = attack-10
        self.defence = defence
        self.magic = magic
        self.moves = ["Attack", "Spell"]

    def damage(self):
        return random.randrange(self.maxattack,self.minattack)
    