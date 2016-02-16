from random import randint

class LoadedDie(object):
    """description of class"""
    
    switchProability = 0.1
  
    def __init__(self, **kwargs):
        self.on = True
        return super().__init__(**kwargs)

    # Chance of getting a 6 is 1/2 while for every other number, chance is 1/10
    def roll(self):
        r = randint(1, 11)
        
        if r > 5:
            return 6
        else:
            return r
    
    # 10% chance that the casino will switch from Loaded to Fair die
    def switch(self):
        if randint(1,11) == 1:
            return True
        else:
            return False

    # Probability that a certain number can be rolled
    @staticmethod
    def probabiltyOfRolling(x):
        if x == 6:
            return 0.5
        else:
            return 0.1

class FairDie(object):
    """Fair die"""
    
    switchProability = 0.05

    def __init__(self, **kwargs):
        self.on = True
        return super().__init__(**kwargs)

    # Fair chance of rolling any number
    def roll(self):
        return randint(1,6)

    # 5% chance that the casino will switch from Fair to Loaded die
    def switch(self):
        if (randint(1,101) % 20) == 0:
            return True
        else:
            return False

    # Probability that a certain number can be rolled
    @staticmethod
    def probabiltyOfRolling(x):
        return 1/6
