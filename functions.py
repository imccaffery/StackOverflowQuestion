import time, random, classes, player
from classes import Skeleton, Rat, Wolf, livingMonsters, monsterlist, Monster
from player import Player




Skeleton()

changemsg = ''
spawnmsg = ''
movemsg = ''
targetmsg = ''
fightmsg = ''
inventorymaxcapacity = 30
winner = None

xMin = 0
xMax = 20

yMin = 0
yMax = 20
#==========================================================================================================================================================#
##Player stuff:

#Creation:
##piero made this already



#Leveling:

def checkExp():
    reqExp = 100 * player.level ** 1.3
    if player.exp == reqExp:
        levelUp(0)
    if player.exp > reqExp:
        levelUp(player.exp-reqExp)
    else:
        pass


    
def levelUp(extraEXP):
    #Increases player level by 1, resets exp, increases hp and dmg by an amount that increases exponentially per level.
    player.level += 1
    player.exp = extraEXP
    player.hp += 10 * 1.1 ** player.level
    player.damage += 5 * 1.1 ** player.level



#Movement

def moveN(player):
    player.y += 1

def moveS(player):
    player.y -= 1

def moveE(player):
    player.x += 1

def moveW(player):
    player.x -= 1

#Items

def pickUp(item, player):
    ##Checks that player inventory is lower than inventory max, a preset variable. If the inventory has room, the item is added to the inventory, deletes item from ground.
    if len(player.inventory) < inventorymaxcapacity:
        player.inventory.append(item)
        delItem(item)
    else:
        print "Your inventory is full! In your foolish attempt to stuff that {} into your pocket, you've broken it.".format(item)



#==========================================================================================================================================================#
##Misc. Functions
def distance(x1, y1, x2, y2):
    ##gives distance between point (x1, y1) and point (x2, y2)
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**.5
    return distance

def changeMSG():
    ##Compiles all program-to-user msg's into one changemsg.
    global changemsg
    changemsg = movemsg + spawnmsg + targetmsg + fightmsg 
    print changemsg
    changemsg = ''
    print livingMonsters
    clearMSG()

def clearMSG():
    global movemsg, spawnmsg, targetmsg, fightmsg
    movemsg, spawnmsg, targetmsg, fightmsg = '','','',''
    

    
    

def keepBoundaries(x1, x2, y1, y2):
    ##Run right before showing map to make sure all monsters stay in bounds.
    for monster in livingMonsters:
        if monster.x < x1:
            monster.x = x1
        if monster.x > x2:
            monster.x = x2
        if monster.y < y1:
            monster.y = y1
        if monster.y > y2:
            monster.y = y2

            

#==========================================================================================================================================================#    
##Monster stuff


def monsterMove():
    global movemsg
    ##Picks a random monster from the list of currently living monsters, and gives it a chance of moving up to 1 unit in both the x and y directions.
    moving = random.choice(livingMonsters)
    if random.randint(0, 1) == 0:
        xchange = random.randint(-2, 2)
        ychange = random.randint(-2, 2)
        moving.x += xchange
        moving.y += ychange

        movemsg = 'something moved'
        monsterSpawn()
        monsterTarget()
    else:

        movemsg = 'nothing moved'
        
def monsterSpawn():
    ##Picks a random type of monster, gives it a chance of being instantiated. 
    global spawnmsg
    spawning = random.choice(monsterlist)
    if random.randint(0, 1) == 0:
        spawning()
        spawnmsg = ' and {} spawned'.format(spawning)
    else:
        spawnmsg = ' and nothing spawned'

def monsterTarget():
    ##Checks if any two monster pairs that have some distance but less than 3 distance from each other exist. If they do, they are told to: fight()
    global targetmsg
    livingMonsters2 = list(livingMonsters)
    for m in livingMonsters:
        m1x = m.x
        m1y = m.y
        for m2 in livingMonsters2:
            m2x = m2.x
            m2y = m2.y
            monsterdistance = distance(m1x, m1y, m2x, m2y)
            if monsterdistance > 0 and monsterdistance < 3:
                if random.randint(0, 4) == 2:
                    fight(m, m2)
                    targetmsg = ' {} attacked {}'.format(m.name, m2.name)

def fight(attacker, attackee):
    ##Finds the winner of a fight between two entities, kill()'s the loser. Winner is set.
    global winner, fightmsg
    numHits1 = attackee.hp / attacker.damage
    numHits2 = attacker.hp / attackee.damage + 1
    if numHits1 < numHits2:
        kill(attackee)
        winner = attacker
        fightmsg = ' and {} won,'.format(attacker.name)
    elif numHits1 == numHits2:
        kill(attacker)
        kill(attackee)
        winner = None
        fightmsg = ' and they both died!'
    else:
        kill(attacker)
        winner = attackee
        fightmsg = ' and {} won,'.format(attackee.name)

def kill(dead):
    ##Sets target's hp to 0, runs makelivingMonsters()
    dead.hp = 0
    makelivingMonsters()



def makelivingMonsters():
    ##Updates livngMonsters[] to only include monsters that are alive(defined as having higher than 0 health in the class module).
    global livingMonsters
    livingMonsters = [x for x in livingMonsters if x.is_alive]




        

def monsterLevel(x):
    ##Useless right now, needs implementation
    x.level += 1
    x.exp = 0
    x.hp += 10 * 1.1 ** player.level
    x.damage += 5 * 1.1 ** player.level







    
#==========================================================================================================================================================#
##Map reader functions:
##use the one we made in class

def drawMap():
    keepBoundaries(xMin, xMax, yMin, yMax)
    for y in xrange(yMin, yMax):
        mapY = y
        for x in xrange(xMin, xMax):
            mapX = x
            flag = False
            for monster in livingMonsters:
                if monster.x == mapX and monster.y == mapY:
                    flag = True
            if flag:
                print '*',
            else:
                print 'O',
        print



    
#==========================================================================================================================================================#
FunctionList1 = [monsterMove]
FunctionList2 = [clearMSG, changeMSG, drawMap]

##def timerepeat(functionList1, functionList2, interval1, interval2):
##    now = time.time()
##    timeElapsed = time.time() - now
##    if timeElapsed % interval1 == 0:
##        for function in functionList1:
##            function()
##    if timeElapsed % interval2 == 0:
##        for function2 in functionList2:
##            function2()
##
##
##
##
##    
##
##    
##while True:
##    timerepeat(FunctionList1, FunctionList2, 5, 10)


    

while True:
    #runs repetitive functions at a time interval(repeatspeed)
    repeatspeed = 1.0
    #here functions are listed:
    movemsg, spawnmsg, targetmsg, fightmsg, = '', '', '', ''
    monsterMove()
    changeMSG()
    x = raw_input(">>> ")
    if x == 'map':
        drawMap()
    
##    starttime = time.time()
##    time.sleep(repeatspeed - ((time.time() - starttime) % repeatspeed))
    
    
    


