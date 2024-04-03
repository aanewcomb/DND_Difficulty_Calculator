import random

class actions:

    #WeaponAttacks

    def sword(attacker,enemies):
        '''for fighter, ranger'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)

    def axe(attacker,enemies):
        '''for barbarian, fighter'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,12)+attacker.aScores[0]
            target.takeDMG(dmg)

    def greatSword(attacker,enemies):
        '''for paladin'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)
    
    def duelWeilding(attacker,enemies): #with two weapon fighting
        '''for fighter'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,4)+attacker.aScores[0]+attacker.prof
            target.takeDMG(dmg)

    def dagger(attacker,enemies):
        '''for rouge'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,4)+attacker.aScores[0]
            target.takeDMG(dmg)

    def rapier(attacker,enemies):
        '''for rouge and druid staff'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(1)
        if roll>=target.ac:
            dmg=random.randint(1,8)+attacker.aScores[1] 
            target.takeDMG(dmg)

    def longbow(attacker,enemies): #with archeryfighting style
        '''for fighter, ranger'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(1)+2
        if roll>=target.ac:
            dmg=random.randint(1,8)+attacker.aScores[1]
            target.takeDMG(dmg)

    def rageAxe(attacker,enemies,rageDie):
        '''for barbarian'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,12)+attacker.aScores[0]+rageDie
            target.takeDMG(dmg)

    def recklessRageAxe(attacker,enemies,rageDie):
        '''for barbarian'''
        target=random.choice(enemies)
        roll=attacker.makeARoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,12)+attacker.aScores[0]+rageDie
            target.takeDMG(dmg)

    def bite(attacker,enemies):
        '''for Wildshape Druid'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,8)+random.randint(1,8)+attacker.aScores[0]
            target.takeDMG(dmg)

    def claw(attacker,enemies):
        '''for Wildshape Druid'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)

    def greatWeaponFightingAxe(attacker,enemies):
        '''for fighter'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,12)
            if dmg==1 or dmg==2:
                dmg=random.randint(1,12)+attacker.aScores[0]
            else:
                dmg+=attacker.aScores[0]
            target.takeDMG(dmg)

    def duelistRapier(attacker,enemies):
        '''for fighter'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(1)
        if roll>=target.ac:
            dmg=random.randint(1,8)+attacker.aScores[1]+2
            target.takeDMG(dmg)

    def unarmedAttack(attacker,enemies,monkDie):
        '''for monk'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(1)
        if roll>=target.ac:
            dmg=random.randint(1,monkDie)+attacker.aScores[1]
            target.takeDMG(dmg)

    def smiteGreatSword(attacker,enemies,smiteDMG):
        '''for paladin'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+random.randint(1,6)+attacker.aScores[0]
            dmg+=random.randint(1,8)+random.randint(1,8)
            for i in range(smiteDMG):
                dmg+=random.randint(1,8)
            target.takeDMG(dmg)

    def hunterMarkLongbow(attacker,enemies): #with archeryfighting style
        '''for fighter, ranger'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(1)+2
        if roll>=target.ac:
            dmg=random.randint(1,8)+attacker.aScores[1]
            target.takeDMG(dmg)

    def sneakDagger(attacker,enemies,sneakDice):
        '''for rouge'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,4)+attacker.aScores[0]
            for i in range(sneakDice):
                dmg+=random.randint(1,6)
            target.takeDMG(dmg)

    #Spells

    #Cantrips
    def viciousMockery(attacker,enemies,insp):
        '''for bard'''
        target=random.choice(enemies)
        roll=target.makeRoll(4)
        if roll>=(attacker.dc+insp):
            dmg=random.randint(1,4)
            target.takeDMG(dmg)

    def sacredFlame(attacker,enemies):
        '''for cleric'''
        target=random.choice(enemies)
        roll=target.makeRoll(1)
        if roll>=(attacker.dc):
            dmg=random.randint(1,8)
            target.takeDMG(dmg)

    def layOnHands(attacker,allies,heal):
        '''for paladin'''
        target=random.choice(allies)
        target.takeHeal(heal)

    def firebolt(attacker,enemies):
        '''for sorcerer'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(5)
        if roll>=target.ac:
            dmg=random.randint(1,10)
            target.takeDMG(dmg)

    def eldritchBlast(attacker,enemies,num):
        '''for warlock'''
        for i in range(num):
            target=random.choice(enemies)
            roll=attacker.makeRoll(5)
            if roll>=target.ac:
                dmg=random.randint(1,10)
                target.takeDMG(dmg)

    def shockingGrasp(attacker,enemies):
        '''for wizard'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(3)
        if roll>=target.ac:
            dmg=random.randint(1,10)
            target.takeDMG(dmg)

    #1st level spells

    def shatter(attacker,enemies,insp):
        '''for bard'''
        target=random.choice(enemies)
        roll=target.makeRoll(4)
        dmg=random.randint(1,8)
        dmg+=random.randint(1,8)
        dmg+=random.randint(1,8)
        if roll>=(attacker.dc+insp):
            dmg=int(dmg/2)
        target.takeDMG(dmg)

    def cureWounds(attacker,allies):
        '''for cleric, druid, ranger'''
        target=random.choice(allies)
        dmg=random.randint(1,8)+attacker.aScores[4]+attacker.prof
        target.takeHeal(dmg)

    def scorchingRays(attacker,enemies):
        '''for sorcerer'''
        for i in range(3):
            target=random.choice(enemies)
            roll=attacker.makeRoll(5)
            if roll>=target.ac:
                dmg=random.randint(1,6)+random.randint(1,6)
                target.takeDMG(dmg)

    def armsOfHadar(attacker,enemies):
        '''for warlock'''
        target=random.choice(enemies)
        roll=target.makeRoll(4)
        dmg=random.randint(1,8)
        dmg+=random.randint(1,8)
        if roll>=(attacker.dc):
            dmg=int(dmg/2)
        target.takeDMG(dmg)

    def magicMissile(attacker,enemies):
        '''for wizard'''
        for i in range(3):
            target=random.choice(enemies)
            dmg=random.randint(1,4)+1
            target.takeDMG(dmg)

    #3-5th level spells

    def charm(attacker,enemies):
        '''for bard'''
        target=random.choice(enemies)
        roll=target.makeRoll(4)
        if roll<=attacker.dc:
            target.ac-=1

    def guidingBolt(attacker,enemies):
        '''for cleric'''
        target=random.choice(enemies)
        roll=attacker.makeARoll(4)
        if roll>=attacker.ac:
            dmg=random.randint(1,8)
            dmg+=random.randint(1,8)
            dmg+=random.randint(1,8)
            dmg+=random.randint(1,8)
            target.takeDMG(dmg)

    def moonbeam(attacker,enemies):
        '''for druid'''
        target=random.choice(enemies)
        roll=target.makeRoll(2)
        dmg=random.randint(1,10)
        dmg+=random.randint(1,10)
        if roll<=(attacker.dc):
            dmg+=random.randint(1,10)
            dmg+=random.randint(1,10)
        target.takeDMG(dmg)

    def conjureVolley(attacker,enemies):
        '''for ranger'''
        dmg=random.randint(1,8)
        for i in range(7):
            dmg+=random.randint(1,8)
        for target in enemies:
            roll=target.makeRoll(1)
            if roll>=attacker.dc:
                dmg=int(dmg/2)
            target.takeDMG(dmg)

    def fireball(attacker,enemies):
        '''for wizard, sorcerer'''
        dmg=random.randint(1,6)
        for i in range(7):
            dmg+=random.randint(1,6)
        for target in enemies:
            roll=target.makeRoll(1)
            if roll>=attacker.dc:
                dmg=int(dmg/2)
            target.takeDMG(dmg)

    def hungerOfHadar(attacker,enemies):
        '''for ranger'''
        dmg=random.randint(1,6)
        for i in range(3):
            dmg+=random.randint(1,6)
        for target in enemies:
            roll=target.makeRoll(2)
            if roll<=attacker.dc:
                dmg+=random.randint(1,6)
                dmg+=random.randint(1,6)
            target.takeDMG(dmg)

    #6th level spell

    def holdMonster(attacker,enemies):
        '''for bard'''
        target=random.choice(enemies)
        roll=target.makeRoll(4)
        if roll<=attacker.dc:
            target.ac-=5

    def spiritGuardians(attacker,enemies):
        '''for cleric'''
        dmg=random.randint(1,8)
        for i in range(4):
            dmg+=random.randint(1,8)
        for target in enemies:
            roll=target.makeRoll(4)
            if roll>=attacker.dc:
                dmg=int(dmg/2)
            target.takeDMG(dmg)

    def blight(attacker,enemies):
        '''for druid'''
        target=random.choice(enemies)
        roll=target.makeRoll(1)
        dmg=random.randint(1,8)
        for i in range(7):
            dmg+=random.randint(1,8)
        if roll>=(attacker.dc):
            dmg=int(dmg/2)
        target.takeDMG(dmg)

    def chainLightning(attacker,enemies):
        '''for sorcerer'''
        target=random.choice(enemies)
        roll=target.makeRoll(2)
        dmg=random.randint(1,8)
        for i in range(9):
            dmg+=random.randint(1,8)
        if roll>=(attacker.dc):
            dmg=int(dmg/2)
        target.takeDMG(dmg)

    def fingerOfDeath(attacker,enemies):
        '''for warlock'''
        target=random.choice(enemies)
        roll=target.makeRoll(2)
        dmg=random.randint(1,8)+30
        for i in range(7):
            dmg+=random.randint(1,8)
        if roll>=(attacker.dc):
            dmg=int(dmg/2)
        target.takeDMG(dmg)

    def disinigrate(attacker,enemies):
        '''for wizard'''
        target=random.choice(enemies)
        roll=target.makeRoll(1)
        dmg=random.randint(1,6)+40
        for i in range(9):
            dmg+=random.randint(1,6)
        if roll>=(attacker.dc):
            dmg=int(dmg/2)
        target.takeDMG(dmg)

    #9th level spell

    def powerWordKill(attacker,enemies):
        '''for bard, warlock'''
        target=random.choice(enemies)
        roll=target.makeRoll(4)
        if target.hp<=100:
            target.alive=False

    def heal(attacker,allies):
        '''for cleric'''
        target=random.choice(allies)
        target.takeHeal(70)

    def sunburst(attacker,enemies):
        '''for druid'''
        dmg=random.randint(1,6)
        for i in range(11):
            dmg+=random.randint(1,6)
        for target in enemies:
            roll=target.makeRoll(4)
            if roll>=attacker.dc:
                dmg=int(dmg/2)
            target.takeDMG(dmg)

    def metorSwarm(attacker,enemies):
        '''for sorcerer, wizard'''
        dmg=random.randint(1,6)
        for i in range(39):
            dmg+=random.randint(1,6)
        for target in enemies:
            roll=target.makeRoll(1)
            if roll>=attacker.dc:
                dmg=int(dmg/2)
            target.takeDMG(dmg)

    #Monster Attacks
    def biteClawClaw(attacker,enemies):
        '''for dragon'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,10)+random.randint(1,10)+attacker.aScores[0]
            target.takeDMG(dmg)
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,6)+random.randint(1,6)+attacker.aScores[0]
            target.takeDMG(dmg)

    def tail(attacker,enemies):
        '''for dragon'''
        target=random.choice(enemies)
        roll=attacker.makeRoll(0)
        if roll>=target.ac:
            dmg=random.randint(1,8)+random.randint(1,8)+attacker.aScores[0]
            target.takeDMG(dmg)

    def dragonBreath(attacker,enemies):
        '''for dragon'''
        dmg=random.randint(1,6)
        for i in range(17):
            dmg+=random.randint(1,6)
        for target in enemies:
            roll=target.makeRoll(1)
            if roll>=attacker.dc:
                dmg=int(dmg/2)
            target.takeDMG(dmg)
