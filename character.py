# character object, will initially set up the variables such as race and name for the user, but the important
# part is to make sure that the list is functional and can have objects added to it as items are secured in the dungeon.

# 19/2/17 Cleaned up all of the objects created here.

class Character(object):
    def __init__(self, name, race, bag):
        self.name = name
        self.race = race
        self.bag = bag

class Monster(object):
   def _init_(self, name, HP):
        self.name = name
        self.HP = HP

