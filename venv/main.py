from classes.game import Player, colors


magic=[{"name":"Thunder Bolt","cost":10,"dmg":80},
       {"name": "Fire Strike", "cost":20 , "dmg":100},
       {"name": "Ice Blast", "cost": 30, "dmg": 120}]

hero=Player(500,150,50,50,magic)
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
        print("You attacked for ",dmg, "points of damage.")
    elif index==1:
        hero.select_magic()
        magic_choice=int(input("Choose a Magic Spell"))-1
        magic_dmg=hero.damage_spell(magic_choice)
        spell=hero.get_spell(magic_choice)
        cost=hero.get_spell_mana(magic_choice)
        current_mana=hero.get_mana()

        if cost>current_mana:
            print(colors.FAIL+"\n Not Enough Mana left\n"+colors.ENDC)
            continue

        hero.reduce_mana(cost)
        enemy.damage_taken(magic_dmg)
        print(colors.OKBLUE+"\n"+spell+" deals",str(magic_dmg)," points of damage"+colors.ENDC)


    enemy_choice=1

    enemy_dmg=enemy.damage()
    hero.damage_taken(enemy_dmg)
    print("Enemy attacks for ",enemy_dmg)

    print("-----------------------------")
    print("Enemy Health:",colors.FAIL+str(enemy.get_health())+"/"+str(enemy.get_maxHealth())+colors.ENDC+"\n")
    print("Your Health:",colors.OKGREEN+str(hero.get_health())+"/"+str(hero.get_maxHealth())+colors.ENDC)
    print("Your Mana:",colors.OKBLUE+str(hero.get_mana())+"/"+str(hero.get_maxMana())+colors.ENDC+"\n")


    if enemy.get_health()==0:
        print(colors.OKGREEN+"You Win!"+colors.ENDC)
        running=False
    elif hero.get_health()==0:
        print(colors.FAIL+"You Died!"+colors.ENDC)
        running=False



