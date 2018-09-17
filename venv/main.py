from classes.game import Player, colors


magic=[{"name":"Thunder Bolt","cost":10,"dmg":30},
       {"name": "Fire Strike", "cost": 15, "dmg": 40},
       {"name": "Ice Blast", "cost": 20, "dmg": 50}]

hero=Player(500,100,50,50,magic)
enemy=Player(1000,100,25,25,magic)

running=True

print(colors.FAIL+colors.BOLD+"You are under attack!"+colors.ENDC)

while running:
    print(colors.FAIL+"---------------------"+colors.ENDC)
    hero.select_action()
    choice=int(input("Choose an Action:"))
    index=choice-1

    if index==0:
        dmg=hero.damage()
        enemy.damage_taken(dmg)
        print("You attacked for ",dmg, "points of damage.  Enemy Health:",enemy.get_health())

    enemy_choice=1

    enemy_dmg=enemy.damage()
    hero.damage_taken(enemy_dmg)
    print("Enemy attacks for ",enemy_dmg,"Your health",hero.get_health())



