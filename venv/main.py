from classes.game import Player, colors
from classes.spells import Spell
from classes.inventory import Item
import random



fire = Spell("Hell Fire", 35, 150, "elemental")
ice = Spell("Ice Blast", 30, 120, "elemental")
thunder = Spell("Thunder Bolt", 10, 75, "elemental")
air = Spell("Air Strike", 20, 100, "elemental")
earth = Spell("Earthquake ", 15,115 , "elemental")

heal=Spell("Heal",8,80,"healing")
resore=Spell("Resore",20,200,"healing")


smpotion=Item("Small Health Potion","potion","Heals 20",20)
lgpotion=Item("Large Health Potion","potion","Heals 100",100)
elixir = Item("Elixir", "elixir", "Fully restores Health and Mana of one team member", 9999)
lgelixir = Item("Large Elixir", "elixir", "Fully restores team's Health and Mana", 9999)

dagger = Item("Dagger", "attack", "Deals 120 damage", 120)
bomb = Item("Bomb", "attack", "Deals 80 damage", 80)


hero_spells=[fire,ice,thunder,air,earth,heal,resore]
hero_items=[{"item":smpotion,"quantity":10},{"item":lgpotion,"quantity":5},{"item":elixir,"quantity":3},{"item":lgelixir,"quantity":1},{"item":dagger,"quantity":5},{"item":bomb,"quantity":8},]

hero1=Player("Tony :",500,150,50,50,hero_spells,hero_items)
hero2=Player("Steve:",500,150,50,50,hero_spells,hero_items)
hero3=Player("John :",500,150,50,50,hero_spells,hero_items)
enemy=Player("Thanos",1000,100,25,25,[],[])

heroes=[hero1,hero2,hero3]

running=True

print(colors.FAIL+colors.BOLD+"You are under attack!"+colors.ENDC)

while running:
    print(colors.FAIL + "---------------------" + colors.ENDC)

    print("\n\n")
    print("NAME              HP                              MP")
    for hero in heroes:

        hero.get_stats()

    print("\n")

    for hero in heroes:
        hero.select_action()
        print()
        choice=int(input("Choose an Action:"))
        index=choice-1

        if index==0:
            dmg=hero.damage()
            enemy.damage_taken(dmg)
            print("You attacked for ",dmg, "points of damage.")
        elif index==1:
            hero.select_magic()
            print()
            magic_choice=int(input("Choose a Magic Spell"))-1

            if magic_choice==-1:
                continue

            spell=hero.magic[magic_choice]
            magic_dmg=spell.spell_damage()


            current_mana=hero.get_mana()

            if spell.cost>current_mana:
                print(colors.FAIL+"\n Not Enough Mana left\n"+colors.ENDC)
                continue

            hero.reduce_mana(spell.cost)

            if spell.type=="healing" or spell.type=="restore":
                hero.heal(magic_dmg)
                print(colors.OKBLUE+"\n"+spell.name+" healed by ",str(magic_dmg),colors.ENDC)
            elif spell.type=="elemental":
                enemy.damage_taken(magic_dmg)
                print(colors.OKBLUE+"\n"+spell.name+" deals",str(magic_dmg)," points of damage"+colors.ENDC)
        elif index==2:
            hero.select_item()
            print()
            item_choice=int(input("Choose an Item from Inventory"))-1

            if item_choice==-1:
                continue

            item=hero.items[item_choice]["item"]
            if hero.items[item_choice]["quantity"]==0:
                print(colors.FAIL+"\n"+"None left..."+colors.ENDC)
                continue
            hero.items[item_choice]["quantity"]-=1




            if item.type=="potion":
                hero.heal(item.prop)
                print(colors.OKGREEN+"\n"+item.name+" healed by ",str(item.prop),colors.ENDC)

            elif item.type=="elixir":
                hero.health=hero.maxhealth
                hero.mana=hero.maxmana
                print(colors.OKGREEN+"\n"+item.name+" fully restored health and mana "+colors.ENDC)
            elif item.type=="attack":
                enemy.damage_taken(item.prop)
                print(colors.FAIL+"\n"+item.name+" deals ",str(item.prop), " damage"+colors.ENDC)

    enemy_choice=1

    enemy_dmg=enemy.damage()
    hero.damage_taken(enemy_dmg)
    print()
    print(colors.FAIL+"Enemy attacks for ",enemy_dmg,colors.ENDC)

    print("-----------------------------")
    print("Enemy Health:",colors.FAIL+str(enemy.get_health())+"/"+str(enemy.get_maxHealth())+colors.ENDC+"\n")

    if enemy.get_health()==0:
        print(colors.OKGREEN+"You Win!"+colors.ENDC)
        running=False
    elif hero.get_health()==0:
        print(colors.FAIL+"You Died!"+colors.ENDC)
        running=False



