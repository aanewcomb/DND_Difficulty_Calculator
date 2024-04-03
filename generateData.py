import random
import numpy as np

from actions import actions
from classes import*
from runEncounter import*

def main():
    data=createData()
    data=toNumpy(data)
    fileControl(data)
    #y = np.loadtxt("dataFile.txt") #DEBUGG
    #print(y) #DEBUGG

def fileControl(data):
    np.savetxt("dataFile.txt",data)

def toNumpy(list):
    npData=np.array(list)
    #print(npData) #DEBUGG
    return npData

def createData():
    data=[]
    for i in range(1000):
        data.append(recordEncounter())
    return data

def recordEncounter():
    allies=[]
    enemies=[]
    data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0] #0:LEVEL 1:BARBARIAN 2:BARD 3:CLERIC 4:DRUID 5:FIGHTER 6:MONK 7:PALADIN 8:RANGER 9:ROUGE 10:SORCERER 11:WARLOCK 12:WIZARD 13:OUTCOME

    lv=random.randint(1,20)
    data[0]=lv

    numOfPlayers=random.randint(2,10)

    for i in range(numOfPlayers):
        playerClass=random.randint(1,12)
        data[playerClass+1]+=1

        if playerClass==0: 
            player=Barbarian(lv)
        elif playerClass==1: 
            player=Bard(lv)
        elif playerClass==2:
            player=Cleric(lv)
        elif playerClass==3:
            player=Druid(lv)
        elif playerClass==4:
            player=Fighter(lv)
        elif playerClass==5:
            player=Monk(lv)
        elif playerClass==6:
            player=Paladin(lv)
        elif playerClass==7:
            player=Ranger(lv)
        elif playerClass==8:
            player=Rouge(lv)
        elif playerClass==9:
            player=Sorcerer(lv)
        elif playerClass==10:
            player=Warlock(lv)
        else:
            player=Wizard(lv)
        
        allies.append(player)

    enemies=generateEnemies()

    data[13]=encounter(allies,enemies)
    #print(data) #DEBUGG
    return data

def generateEnemies():
    e=[Dragon()]
    #e=[Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin(),Goblin()]
    return e
    
main()
            
#creates the allies list
    #random num for amount of players from 2-10
    #randomly selects class for each player

#creates the enemy list
    #either dragon or twenty goblins