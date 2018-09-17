from classes.game import Player, colors


magic=[{"name":"Thunder Bolt","cost":10,"dmg":30},
       {"name": "Fire Strike", "cost": 15, "dmg": 40},
       {"name": "Ice Blast", "cost": 20, "dmg": 50}]

hero=Player(500,100,50,50,magic)
enemy=Player(1200,100,25,25,magic)

running=True

print(colors.FAIL+colors.BOLD+"You are under attack!"+colors.ENDC)

while running:
    print(colors.FAIL+"---------------------"+colors.ENDC)
    hero.select_action()
    running=False


