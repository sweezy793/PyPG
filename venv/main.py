from classes.game import Player, colors


magic=[{"name":"Thunder Bolt","cost":10,"dmg":30},
       {"name": "Fire Strike", "cost": 15, "dmg": 40},
       {"name": "Ice Blast", "cost": 20, "dmg": 50}]

player=Player(500,100,50,50,magic)


print(player.damage())
print(player.damage())
print(player.damage())
