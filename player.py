def Player():
    def __init__(self, name, hp, damage, exp, level, inventory, x, y):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.exp = exp
        self.level = level
        self.inventory = inventory
        self.x = x
        self.y = y

        self.inventory = []
        
        playerList.append(self)

    def __str__(self):
        return "Level {} player named {}".format(self.level, self.name)
    
        
        
