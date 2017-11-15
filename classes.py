xMin = 0
xMax = 20

yMin = 0
yMax = 20

import random
livingMonsters = []
class Monster(object):
    def __init__(self, name, hp, damage, x, y, exp, level):
        """Creates a new enemy

        name: name of the enemy
        hp: hit points of the enemy
        damage: the per-hit damage the enemy does
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.x = x
        self.y = y
        self.exp = exp
        self.level = level

        x = random.randint(xMin, xMax)
        y = random.randint(yMin, yMax)

        livingMonsters.append(self)
        print self.name, "just got added"
    def is_alive(self):
        if self.hp > 0:
            return True

    def __str__(self):
        return "{} \n===================\nName: {}\nHP: {}\nDMG: {}\n(X,Y):({},{})".format(self.name, self.hp, self.damage, self.x, self.y)

class Rat(Monster):
    def __init__(self):
        super(Rat, self).__init__(name='Rat', hp=5, damage=2, x=0, y=0, exp = 0, level = 0)

class Wolf(Monster):
    def __init__(self):
        super(Wolf, self).__init__(name='Wolf', hp=8, damage=4, x=0, y=0, exp = 0, level = 0)

class Skeleton(Monster):
    def __init__(self):
        super(Skeleton, self).__init__(name='Skeleton', hp=20, damage=4, x=0, y=0, exp = 0, level = 0)


monsterlist = [Skeleton, Wolf, Rat]

        




    
                                      
        

