import random

from actions import actions

class Creature:
    maxHp=1
    hp=1
    ac=8
    dc=8
    aScores=[10,10,10,10,10,10] #0:STR 1:DEX 2:CON 3:INT 4:WIS 5:CHA
    prof=2
    alive=True

    def makeRoll(self, score):
        roll=random.randint(1,20)+self.aScores[score]+self.prof
        return roll
    
    def makeARoll(self, score):
        roll=random.randint(1,20)+self.aScores[score]+self.prof
        roll2=random.randint(1,20)+self.aScores[score]+self.prof
        if roll2>roll:
            roll=roll2
        return roll
    
    def makeDRoll(self, score):
        roll=random.randint(1,20)+self.aScores[score]+self.prof
        roll2=random.randint(1,20)+self.aScores[score]+self.prof
        if roll2<roll:
            roll=roll2
        return roll
    
    def takeDMG(self, dmg):
        self.hp-=dmg
        if self.hp<1:
            self.alive=False
            #print(self,"was defeated") #DEBUG

    def takeHeal(self, heal):
        self.hp+=heal
        if self.hp<self.maxHp:
            self.hp=self.maxHp

    def printStats(self):
        print("STR:", self.aScores[0]," DEX:", self.aScores[1]," CON:", self.aScores[2]," INT:", self.aScores[3]," WIS:", self.aScores[4]," CHA:", self.aScores[5])
        print("Hit Points:",self.hp,"/",self.maxHp)
        print("AC:",self.ac)

class Character(Creature):
    lv=1

class Barbarian(Character):
    rage=2

    def __init__(self, lv):
        self.aScores=[5,3,4,0,0,0]
        self.lv=lv
        self.maxHp=int(((7*lv)+(self.aScores[2]*lv))*1.5)
        self.hp=self.maxHp
        self.ac=10+self.aScores[1]+self.aScores[2]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv>8:
            self.rage=3
        elif self.lv>15:
            self.rage=4

    def takeTurn(self,allies,enemies):
        if self.lv<5:
            self.takeAction(allies,enemies)
        else:
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==3 or choice==6 or choice==10:
            actions.axe(self,enemies)
        elif choice==2 or choice==4 or choice==5 or choice==7 or choice==8 or choice==11 or choice==12 or choice==14 or choice==17:
            actions.rageAxe(self,enemies,self.rage)
        else:
            actions.recklessRageAxe(self,enemies,self.rage)

class Bard(Character):
    insp=6

    def __init__(self, lv):
        self.aScores=[0,3,2,1,1,5]
        self.lv=lv
        self.maxHp=int(((4*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=11+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv>4:
            self.insp=8
        elif self.lv>9:
            self.insp=10
        elif self.lv>14:
            self.insp=12
    
        self.dc=8+self.aScores[5]+self.prof

    def bardicInsp(self):
        inspiration=random.randint(1,self.insp)
        return inspiration
    
    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==2 or choice==4 or choice==5 or choice==7 or choice==11 or choice==13 or choice==16:
            actions.viciousMockery(self,enemies,self.bardicInsp())
        elif choice==3 or choice==6 or choice==9 or choice==12 or choice==18:
            actions.shatter(self,enemies, self.bardicInsp())
        elif choice==5 or choice==8 or choice==14 or choice==19:
            actions.charm(self,enemies)
        elif choice==10 or choice==15 or choice==20:
            actions.holdMonster(self,enemies)
        else: #17
            actions.powerWordKill(self,enemies)

class Cleric(Character):

    def __init__(self, lv):
        self.aScores=[1,2,2,1,5,0]
        self.lv=lv
        self.maxHp=int(((5*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=14+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        self.dc=8+self.aScores[4]+self.prof

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==2 or choice==4 or choice==5 or choice==7 or choice==11 or choice==13 or choice==16:
            actions.sacredFlame(self,enemies)
        elif choice==3 or choice==6 or choice==9 or choice==12 or choice==18:
            actions.cureWounds(self,allies)
        elif choice==5 or choice==8 or choice==14 or choice==19:
            actions.guidingBolt(self,enemies)
        elif choice==10 or choice==15 or choice==20:
            actions.spiritGuardians(self,enemies)
        else: #17
            actions.heal(self,allies)

class Druid(Character):
    wildshape=False
    wsCount=0
    wsHP=10

    def __init__(self, lv):
        self.aScores=[2,2,3,0,5,0]
        self.lv=lv
        self.maxHp=int(((5*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=10+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv>2:
            self.wsCount=2

        self.dc=8+self.aScores[4]+self.prof

    def takeDMG(self, dmg):
        if self.wildshape:
            self.wsHP-=dmg
            if self.wsHP<1:
                self.wildshape=False
        else:
            self.hp-=dmg
        if self.hp<1:
            self.alive=False

    def takeWildshape(self):
        self.wsHP=int(self.lv/2)*10
        self.wildshape=True
        self.wsCount-=1

    def takeTurn(self,allies,enemies):
        if self.wildshape:
            if self.lv<11:
                self.takeWSAction(allies,enemies)
            else:
                self.takeWSAction(allies,enemies)
                self.takeWSAction(allies,enemies)
        else:
            if self.wsCount>0:
                choice=random.randint(0,1)
                if choice == 0:
                    self.takeAction(allies,enemies)
                else:
                    self.takeWildshape()
            else:
                self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==2 or choice==4 or choice==5 or choice==7 or choice==11 or choice==13 or choice==16:
            actions.rapier(self,enemies)
        elif choice==3 or choice==6 or choice==9 or choice==12 or choice==18:
            actions.cureWounds(self,allies)
        elif choice==5 or choice==8 or choice==14 or choice==19:
            actions.moonbeam(self,enemies)
        elif choice==10 or choice==15 or choice==20:
            actions.blight(self,enemies)
        else: #17
            actions.sunburst(self,allies)

    def takeWSAction(self,allies,enemies):
        choice=random.randint(0,1)
        if choice == 0:
            actions.bite(self,enemies)
        else:
            actions.claw(self,enemies)

class Fighter(Character):
    weaponType=0

    def __init__(self, lv):
        self.aScores=[5,3,4,0,0,0]
        self.lv=lv
        self.maxHp=int(((6*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=16

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        type=random.randint(0,5)
        self.weaponType=type

        if type==0: #sheild and sword
            self.ac+=2
        elif type==1: #axe
            pass
        elif type==2: #greatsword
            self.ac+=1
        elif type==3: #duelweilding
            pass
        elif type==4: #duelist
            self.aScores=[3,5,4,0,0,0]
        else: #archery
            self.aScores=[3,5,4,0,0,0]

    def takeTurn(self,allies,enemies):
        if self.lv<5:
            self.takeAction(allies,enemies)
        elif self.lv<11:
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)
        elif self.lv<20:
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        if self.weaponType==0: #sheild and sword
            actions.sword(self,enemies)
        elif self.weaponType==1: #axe
            actions.greatWeaponFightingAxe
        elif self.weaponType==2: #greatsword
            actions.greatSword
        elif self.weaponType==3: #duelweilding
            actions.duelWeilding
        elif self.weaponType==4: #duelist
            actions.duelistRapier
        else: #archery
            actions.longbow

class Monk(Character):
    martialArts=4

    def __init__(self, lv):
        self.aScores=[0,5,2,1,4,0]
        self.lv=lv
        self.maxHp=int(((5*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=10+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv<11:
            self.martialArts=6
        elif self.lv<17:
            self.prof=8
        else: #17 or higher
            self.prof=10

        self.dc=8+self.aScores[4]+self.prof

    def takeTurn(self,allies,enemies):
        if self.lv<5:
            self.takeAction(allies,enemies)
        else:
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==3 or choice==6 or choice==10:
            actions.unarmedAttack(self,enemies,self.martialArts)
        elif choice==2 or choice==4 or choice==5 or choice==7 or choice==8 or choice==11 or choice==12 or choice==14 or choice==17:
            actions.unarmedAttack(self,enemies,self.martialArts)
            actions.unarmedAttack(self,enemies,self.martialArts)
            actions.unarmedAttack(self,enemies,self.martialArts)
        else:
            actions.unarmedAttack(self,enemies,self.martialArts)
            actions.unarmedAttack(self,enemies,self.martialArts)
            actions.unarmedAttack(self,enemies,self.martialArts)
            actions.unarmedAttack(self,enemies,self.martialArts)

class Paladin(Character):
    smiteCount=0
    smiteDmg=1

    def __init__(self, lv):
        self.aScores=[5,0,3,0,0,4]
        self.lv=lv
        self.maxHp=int(((6*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=16

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv<2:
            self.smiteCount=0
        elif self.lv<3:
            self.smiteCount=2
        elif self.lv<5:
            self.smiteCount=3
        elif self.lv<7:
            self.smiteCount=6
            self.smiteDmg=2
        elif self.lv<13:
            self.smiteCount=9
            self.smiteDmg=3
        elif self.lv<17:
            self.smiteCount=11
            self.smiteDmg=4
        else:
            self.smiteCount=14
            self.smiteDmg=5

        self.dc=8+self.aScores[5]+self.prof

    def takeTurn(self,allies,enemies):
        if self.lv<5:
            self.takeAction(allies,enemies)
        else:
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        if self.smiteCount>0:
            choice=random.randint(1,self.lv)
            if choice==2 or choice==5 or choice==10 or choice==12 or choice==15 or choice==17:
                actions.smiteGreatSword(self,enemies,random.randint(1,self.smiteDmg))
            elif choice==3 or choice==6 or choice==11 or choice==13 or choice==16:
                healed=random.randint(1,self.lv)
                actions.layOnHands(self,allies,healed)
            else:
                actions.greatSword(self,enemies)
        else:
            choice=random.randint(1,self.lv)
            if choice==3 or choice==6 or choice==11 or choice==13 or choice==16:
                healed=random.randint(1,self.lv)
                actions.layOnHands(self,allies,healed)
            else:
                actions.greatSword(self,enemies)

class Ranger(Character):

    def __init__(self, lv):
        self.aScores=[1,5,2,0,4,0]
        self.lv=lv
        self.maxHp=int(((6*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=10+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        self.dc=8+self.aScores[4]+self.prof

    def takeTurn(self,allies,enemies):
        if self.lv<5:
            self.takeAction(allies,enemies)
        else:
            self.takeAction(allies,enemies)
            self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==2 or choice==4  or choice==7 or choice==9 or choice==11 or choice==13 or choice==16 or choice==19 or choice==20:
            actions.hunterMarkLongbow(self,enemies)
        elif choice==3 or choice==6  or choice==18:
            actions.cureWounds(self,allies)
        elif choice==17:
            actions.conjureVolley(self,enemies)
        else: 
            choice=random.randint(0,1)
            if choice==0:
                actions.longbow
            else:
                actions.sword

class Rouge(Character):
    sneakDice=1

    def __init__(self, lv):
        self.aScores=[0,5,2,3,2,0]
        self.lv=lv
        self.maxHp=int(((5*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=11+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv<3:
            self.sneakDice=1
        elif self.lv<5:
            self.sneakDice=2
        elif self.lv<7:
            self.sneakDice=3
        elif self.lv<9:
            self.sneakDice=4
        elif self.lv<11:
            self.sneakDice=5
        elif self.lv<13:
            self.sneakDice=6
        elif self.lv<15:
            self.sneakDice=7
        elif self.lv<17:
            self.sneakDice=8
        elif self.lv<19:
            self.sneakDice=9
        else:
            self.sneakDice=10

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==3 or choice==6 or choice==10:
            actions.dagger(self,enemies)
        elif choice==2 or choice==4 or choice==5 or choice==7 or choice==8 or choice==11 or choice==12 or choice==14 or choice==17:
            actions.rapier(self,enemies)
        else:
            actions.sneakDagger(self,enemies,self.sneakDice)

class Sorcerer(Character):

    def __init__(self, lv):
        self.aScores=[0,4,3,0,0,5]
        self.lv=lv
        self.maxHp=int(((4*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=10+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        self.dc=8+self.aScores[5]+self.prof

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==2 or choice==4 or choice==5 or choice==7 or choice==11 or choice==13 or choice==16:
            actions.firebolt(self,enemies)
        elif choice==3 or choice==6 or choice==9 or choice==12 or choice==18:
            actions.scorchingRays(self,allies)
        elif choice==5 or choice==8 or choice==14 or choice==19:
            actions.fireball(self,enemies)
        elif choice==10 or choice==15 or choice==20:
            actions.chainLightning(self,enemies)
        else: #17
            actions.metorSwarm(self,allies)

class Warlock(Character):
    blasts=1

    def __init__(self, lv):
        self.aScores=[0,3,4,0,0,5]
        self.lv=lv
        self.maxHp=int(((5*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=11+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        if self.lv<5:
            self.blasts=1
        elif self.lv<11:
            self.blasts=2
        else:
            self.blasts=3

        self.dc=8+self.aScores[5]+self.prof

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==2:
            actions.armsOfHadar(self,enemies)
        elif choice==5:
            actions.hungerOfHadar(self,allies)
        elif choice==10:
            actions.fingerOfDeath(self,enemies)
        elif choice==17:
            actions.powerWordKill(self,enemies)
        else: #17
            actions.eldritchBlast(self,allies,self.blasts)

class Wizard(Character):

    def __init__(self, lv):
        self.aScores=[0,4,3,5,0,0]
        self.lv=lv
        self.maxHp=int(((4*lv)+(self.aScores[2]*lv)))
        self.hp=self.maxHp
        self.ac=10+self.aScores[1]

        if self.lv<5:
            self.prof=2
        elif self.lv<9:
            self.prof=3
        elif self.lv<13:
            self.prof=4
        elif self.lv<17:
            self.prof=5
        else:
            self.prof=6

        self.dc=8+self.aScores[3]+self.prof

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,self.lv)
        if choice==1 or choice==2 or choice==4 or choice==5 or choice==7 or choice==11 or choice==13 or choice==16:
            actions.shockingGrasp(self,enemies)
        elif choice==3 or choice==6 or choice==9 or choice==12 or choice==18:
            actions.magicMissile(self,allies)
        elif choice==5 or choice==8 or choice==14 or choice==19:
            actions.fireball(self,enemies)
        elif choice==10 or choice==15 or choice==20:
            actions.disinigrate(self,enemies)
        else: #17
            actions.metorSwarm(self,allies)

class Monster(Creature):
    crRate="1"

class Dragon(Monster):

    def __init__(self):
        self.aScores=[8,0,7,3,1,5]
        self.maxHp= 256
        self.hp=self.maxHp
        self.ac=19
        self.prof=6
        self.dc=18
        self.crRate="17"

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        choice=random.randint(1,20)
        if choice==1 or choice==3 or choice==6 or choice==10:
            actions.biteClawClaw(self,allies)
        elif choice==2 or choice==4 or choice==5 or choice==7 or choice==8 or choice==11 or choice==12 or choice==14 or choice==17:
            actions.biteClawClaw(self,allies)
            actions.tail(self,allies)
        else:
            actions.dragonBreath(self,allies)

class Goblin(Monster):

    def __init__(self):
        self.aScores=[0,2,0,0,0,0]
        self.maxHp= 7
        self.hp=self.maxHp
        self.ac=15
        self.prof=2
        self.crRate="1/4"

    def takeTurn(self,allies,enemies):
        self.takeAction(allies,enemies)

    def takeAction(self,allies,enemies):
        actions.sword(self,allies)


'''player=Bard(10)
monster1=Dragon()
monster2=Dragon()
monster3=Dragon()
player.takeTurn([player],[monster1,monster2,monster3])
player.takeTurn([player],[monster1,monster2,monster3])
player.takeTurn([player],[monster1,monster2,monster3])
player.takeTurn([player],[monster1,monster2,monster3])
#actions.holdMoster(player,[monster])

monster1.printStats()
monster2.printStats()
monster3.printStats()'''

