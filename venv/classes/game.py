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
    def __init__(self,name,health,mana,attack,defence,magic,items):
        self.maxhealth = health
        self.health = health
        self.maxmana = mana
        self.mana = mana
        self.maxattack = attack+10
        self.minattack = attack-10
        self.defence = defence
        self.magic = magic
        self.items=items
        self.actions = ["Melee Attack", "Magic Spell","Inventory"]
        self.name=name

    def damage(self):
        return random.randrange(self.minattack,self.maxattack)



    def damage_taken(self,dmg):
        self.health-=dmg
        if self.health<0:
            self.health=0
        return self.health

    def heal(self,dmg):
        self.health+=dmg
        if self.health>self.maxhealth:
            self.health=self.maxhealth

    def get_health(self):
        return self.health

    def get_maxHealth(self):
        return self.maxhealth

    def get_mana(self):
        return self.mana

    def get_maxMana(self):
        return self.maxmana

    def reduce_mana(self,cost):
        self.mana-=cost



    def select_action(self):
        i=1
        print()
        print(colors.OKGREEN+colors.BOLD+"ACTIONS"+colors.ENDC)
        print()
        for item in self.actions:
            print("     " +str(i)+":", item)
            i+=1

    def select_magic(self):
        i=1
        print()
        print(colors.OKBLUE+"SPELLS")
        print("------"+colors.ENDC)
        for spell in self.magic:
            print("     " +str(i)+")",spell.name,"(cost:",str(spell.cost)+")")
            i+=1

    def select_item(self):
        i=1
        print()
        print(colors.OKBLUE+"INVENTORY")
        print("---------"+colors.ENDC)
        for item in self.items:
            print("     " +str(i)+")",item["item"].name,":",item["item"].description,"(x"+str(item["quantity"])+")")
            i+=1

    def get_stats(self):
        print("                  ___________________             __________")
        print(colors.BOLD+self.name+"   "+str(self.health)+"/"+str(self.maxhealth)+ " "+"|"+colors.OKGREEN+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+colors.ENDC+"|" + "    " +colors.BOLD+ str(self.mana)+"/"+str(self.maxmana)+"|"+colors.OKBLUE+"▓▓▓▓▓▓▓▓▓▓"+colors.ENDC+"|")

