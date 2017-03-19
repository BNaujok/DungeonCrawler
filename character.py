# character object, will initially set up the variables such as race and name for the user, but the important
# part is to make sure that the list is functional and can have objects added to it as items are secured in the dungeon.

class character(object):

    name = "Brain"
    race = "Oxymoron warrior"
    bag = [0]*10

    def __init__(self, name, race, bag):
        self.name = name
        self.age = race
        self.major = bag

def make_character(name, race, bag):
    character = character(name, age, major)
    return character


class monster(object):
    name = ""

    def _init_(self, name):
        self.name = name

def make_dungeonrat(name):
    monster = monster("dungeon rat")
    return monster

