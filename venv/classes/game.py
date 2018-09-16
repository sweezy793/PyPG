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
        return random.randrange(self.minattack,self.maxattack)

    def damage_spell(self,i):
        maxmag=self.magic[i]["dmg"]+5
        minmag=self.magic[i]["dmg"]-5
        return random.randrange(minmag,maxmag)

    def damage_done(self,dmg):
        self.health-=dmg
        if self.health<0:
            self.health=0
        return self.health

    def get_health(self):
        return self.health

    def get_maxHealth(self):
        return self.maxhealth

    def get_mana(self):
        return self.mana

    def get_maxMana(self):
        return self.maxmana

    def mana_cost(self):
        self.mana-=cost

    def get_spell(self,i):
        return self.magic[i]["name"]

    def get_spell_mana(self,i):
        return self.magic[i]["cost"]

    