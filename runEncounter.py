import random

from actions import actions
from classes import*

def encounter(allies,enemies):
    running=True
    initiative=rollInitiative(allies,enemies)
    while(running):
        for i in initiative:
            if initiative[i].alive:
                #print(initiative[i],"is taking a turn") #DEBUG
                initiative[i].takeTurn(allies,enemies)
                checkForDead(allies,enemies)
                running=checkForEnd(allies,enemies)
                if not running:
                    break
    
    return checkOutcome(allies,enemies)

def rollInitiative(allies,enemies):
    init={}
    all=allies+enemies
    for i in range(len(all)):
        choice=random.choice(all)
        init[i]=choice
        all.remove(choice)
    return init

def checkForDead(allies,enemies):
    for i in allies:
        if i.alive==False:
            allies.remove(i)
    for i in enemies:
        if i.alive==False:
            enemies.remove(i)

def checkForEnd(allies,enemies):
    if len(allies)==0:
        return False
    elif len(enemies)==0:
        return False
    else:
        return True

def checkOutcome(allies,enemies):
    if len(allies)>0:
        return 1
    else:
        return 0

'''a1=Barbarian(20)
a2=Bard(20)
a3=Cleric(20)
a4=Druid(20)
a5=Fighter(20)
a6=Monk(20)
a7=Paladin(20)
a8=Ranger(20)
a9=Rouge(20)
a10=Sorcerer(20)
a11=Warlock(20)
a12=Wizard(20)

a=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]

e1=Dragon()
e2=Dragon()
e3=Dragon()
e4=Goblin()
e5=Goblin()
e6=Goblin()
e7=Goblin()
e8=Goblin()

e=[e1,e2,e3,e4,e5,e6,e7,e8]

print(encounter(a,e))'''
