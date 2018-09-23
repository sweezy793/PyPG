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
        print("\n"+"     "+colors.BOLD+self.name+colors.ENDC)
        print(colors.OKGREEN+colors.BOLD+"     ACTIONS"+colors.ENDC)
        print()
        for item in self.actions:
            print("         " +str(i)+":", item)
            i+=1

    def select_magic(self):
        i=1
        print()
        print(colors.OKBLUE+"     SPELLS")
        print("     ------"+colors.ENDC)
        for spell in self.magic:
            print("         " +str(i)+")",spell.name,"(cost:",str(spell.cost)+")")
            i+=1

    def select_item(self):
        i=1
        print()
        print(colors.OKBLUE+"     INVENTORY")
        print("     ---------"+colors.ENDC)
        for item in self.items:
            print("         " +str(i)+")",item["item"].name,":",item["item"].description,"(x"+str(item["quantity"])+")")
            i+=1
    def get_enemy_stats(self):
        hp_bar=""
        bar_ticks=(self.health/self.maxhealth)*100/2
        while bar_ticks>0:
            hp_bar+="▓"
            bar_ticks-=1
        while len(hp_bar)<50:
            hp_bar+=" "

        health_string = str(self.health) + "/" + str(self.maxhealth)
        current_health = ""
        if len(health_string) < 9:
            decreased = 9 - len(health_string)

            while decreased > 0:
                current_health += " "
                decreased -= 1

            current_health += health_string
        else:
            current_health = health_string

        print("                     __________________________________________________")
        print(colors.BOLD + self.name + "   " + current_health + " " + "|" + colors.FAIL + hp_bar + colors.ENDC + "|" )

    def get_stats(self):
        hp_bar=""
        bar_ticks=(self.health/self.maxhealth)*100/4

        mp_bar=""
        mp_ticks=(self.mana/self.maxmana)*100/10

        while bar_ticks>0:
            hp_bar+="▓"
            bar_ticks-=1
        while len(hp_bar)<25:
            hp_bar+=" "

        while mp_ticks>0:
            mp_bar+="▓"
            mp_ticks-=1

        while len(mp_bar)<10:
            mp_bar+=" "

        health_string=str(self.health)+"/"+str(self.maxhealth)
        current_health=""
        if len(health_string)<7:
            decreased=7-len(health_string)

            while decreased >0:
                current_health+=" "
                decreased-=1

            current_health+=health_string
        else:
            current_health=health_string

        mana_string=str(self.mana)+"/"+str(self.maxmana)
        current_mana=""

        if len(mana_string)<7:
            decreased=7-len(mana_string)
            while decreased>0:
                current_mana+=" "
                decreased-=1
            current_mana+=mana_string
        else:
            current_mana=mana_string

        print("                   _________________________             __________")
        print(colors.BOLD+self.name+"   "+current_health+ " "+"|"+colors.OKGREEN+hp_bar+colors.ENDC+"|" + "    " +colors.BOLD+ current_mana+"|"+colors.OKBLUE+mp_bar+colors.ENDC+"|")

