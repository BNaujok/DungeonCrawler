# Currently this is the navigation file for the dungeon.
# 9/2/2017 dungeon is at a single level with varied length halls in which you can travel in either direction using cardinal points
# Need random item/encounter functionality to be built into the program.
# 23/4/17 Finally completed basic room code structure.
# 26/9/17 Established logging protocols to assist me to debug and track the progress of the code
# 5/10/17 Finalised the encounter protocols with monsters

import sys
import character
import monster
import logging


# setting logging level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a log file for navigation
handler = logging.FileHandler('nav.log')
handler.setLevel(logging.DEBUG)

# add handler to the logger
logger.addHandler(handler)

class Location:
    def _init_(self, north=None,south=None,east=None,west=None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

direction = ""

def move_question():
    global direction

    if character.Character.knife == 'true':
        monster.random_encounter()
        
    direction = input("Which direction do you want to go? ")
    logger.debug('Direction given: %s', direction)
#    logger.info('sending direction back to the function below...')
    if direction == "exit":
        sys.exit()
    else:
        return(direction)

    


def room_description():
    print("You have entered into a large chamber.")
#    print("There are no other exits other than the one you just came through")

def tunnel():
    print("You find yourself walking through a damp and darkened tunnel")
    
def dead_end():
    print("You are staring at a dead end with no where to go.")

        
def entrance():
    room_description()
    move_question()
    logger.info('In the entrance')
    if direction == "n":
        hall3()
    elif direction == "w":
        hall2()
    elif direction == "e":
        hall1()
    else:
        print("Please enter n, e or w for your movement.")
        entrance()

def hall1():
    tunnel()
    move_question()
    logger.info('In hall1')
    if direction == "e":
        hall1a()
    elif direction == "w":
        entrance()
    else:
        dead_end()
        hall1()
        
        
def hall1a():
    tunnel()
    move_question()
    logger.info('In hall1a')
    if direction == "e":
        room1()
    elif direction == "w":
        hall1()
    else:
        dead_end()
        hall1a()


def room1():
#  Need to check to see if there is a knife in the bag from this point. As it will change the print statements called.
#   if character.character.bag
    logger.info('In room 1')
    room_description()

    move_question()

    logging.debug('returned info %s', direction)

    if direction == "w":
        hall1a()
    elif direction == "look":
        o = input("There is a knife lying on the ground. What would you like to do?")
        logging.debug('%s', o)
        
        if o == "pickup knife":
            character.Character.knife = "true"
            logger.debug('knife status %s', character.Character.knife)
            print("the knife has been placed into your bag")
            room1()
        else:
            room1()
    elif direction == "e" or direction == "n" or direction == "s":
        dead_end()
        room1()
    else:
        print("That is not a valid command")
        room1()

def hall2():
    logger.info('In hall 2')
    
    tunnel()
    move_question()

    if direction == "e":
        entrance()
    elif direction == "w":
        hall2a()
    else:
        dead_end()
        hall2()
    
                  
def hall2a():
    logger.info('In hall 2a')
    
    tunnel()
    move_question()

    if direction == "e":
        hall2()
    elif direction == "w":
        hall2b()
    else:
        dead_end()
        hall2a()


def hall2b():
    logger.info('In hall 2b')
    
    tunnel()
    move_question()

    if direction == "e":
        hall2a()

    else:
        dead_end()
        hall2b()

def hall3():
    logger.info('In hall 3')
    
    tunnel()
    move_question()

    if direction == "n":
        hall3a()

    elif direction == "s":
        entrance()

    else:
        dead_end()
        hall3()

def hall3a():
    logger.info('In hall 3a')
    
    tunnel()
    move_question()

    if direction == "n":
        hall3b()
    elif direction == "s":
        hall3()
    else:
        dead_end()
        hall3a()

def hall3b():
    logger.info('In hall 3b')
    
    tunnel()
    move_question()

    if direction == "n":
        hall3c()
    elif direction == "s":
        hall3a()
    elif direction == "e":
        hall4()
    elif direction == "w":
        hall6()
    else:
        print("Please enter n, s, e or w for a valid direction")
        hall3b()
            
def hall3c():
    logger.info('In hall 3c')
    
    tunnel()
    move_question()

    if direction == "n":
        hall3d()
    elif direction == "s":
        hall3b()
    else:
        dead_end()
        hall3c()

def hall3d():
    logger.info('In hall 3d')
    
    tunnel()
    move_question()

    if direction == "n":
        hall3e()
    elif direction == "s":
        hall3c()
    else:
        dead_end()
        hall3d()

def hall3e():
    logger.info('In hall 3e')
    
    tunnel()
    move_question()

    if direction == "n":
        hall3f()
    elif direction == "s":
        hall3d()
    elif direction == "e":
        hall5()
    else:
        dead_end()
        hall3e()

def hall3f():
    logger.info('In hall 3f')
    
    tunnel()
    move_question()

    if direction == "n":
        room4()
    elif direction == "s":
        hall3e()
    else:
        dead_end()
        hall3f()

def room4():

    logger.info('In room 4')
    
    cheststatus = "locked"
    room_description()
    
    move_question()

    if direction == "s":
        hall3f()
    elif direction == "look":
        o = input("There is a chest in the corner of the room. What would you like to do?")
        if o == "open chest":
            if cheststatus == "locked":
                print("the chest is locked")
                room4()
            else:
                print("You have found some useless treasure! Congratulations")
                
        elif o == "unlock chest":
            if character.Character.key == "false":
                print("You don't have a key to open the chest. Explore until you find it.")
            else:
                cheststatus = "unlocked"
 
    elif direction == "e" or "n" or "s":
        dead_end()
        room4()

    else:
        print("That is not a valid command")
        room4()
    
def hall4():
    logger.info('In hall 4')
    
    tunnel()
    move_question()

    if direction == "e":
        hall4a()
    elif direction == "w":
        hall3b()
    else:
        dead_end()
        hall4()

def hall4a():
    logger.info('In hall 4a')
    
    tunnel()
    move_question()

    if direction == "e":
        hall4b()
    elif direction == "w":
        hall4()
    else:
        dead_end()
        hall4a()

def hall4b():
    logger.info('In hall 4b')
    
    tunnel()
    move_question()

    if direction == "e":
        room2()
    elif direction == "w":
        hall4a()
    else:
        dead_end()
        hall4b()

def room2():

    logger.info('In room 2')
    
    room_description()
    move_question()

    if direction == "w":
        hall4b()
    else:
        dead_end()
        room2()

        
def hall6():
    logger.info('In hall 6')
    
    tunnel()
    move_question()

    if direction == "e":
        hall3b()
    elif direction == "w":
        hall6a()
    else:
        dead_end()
        hall6()

def hall6a():
    logger.info('In hall 6a')
    
    tunnel()
    move_question()

    if direction == "e":
        hall6()
    elif direction == "w":
        room3()
    else:
        dead_end()
        hall6a()

def room3():
    logger.info('In room 3')
    
    room_description()
    
    move_question()

    if direction == "w":
        hall8()
    elif direction == "n":
        hall7()
    elif direction == "e":
        hall6a()
    else:
        dead_end()
        room3()
        
def hall8():
    logger.info('In hall 8')
    
    tunnel()
    move_question()

    if direction == "e":
        room3()
    elif direction == "w":
        hall8a()
    else:
        dead_end()
        hall8()

def hall8a():
    logger.info('In hall 8a')
    
    tunnel()
    move_question()

    if direction == "e":
        hall8()
    elif direction == "n":
        hall9c()
    elif direction == "s":
        hall9b()
    else:
        dead_end()
        hall8a()

def hall9():
    logger.info('In hall 9')
    
    tunnel()
    move_question()

    if direction == "n":
        hall9a()
    else:
        dead_end()
        hall9()

def hall9a():
    logger.info('In hall 9a')
    
    tunnel()
    move_question()

    if direction == "n":
        hall9b()
    elif direction == "s":
        hall9()
    else:
        dead_end()
        hall9a()

def hall9b():
    logger.info('In hall 9b')
    
    tunnel()
    move_question()

    if direction == "n":
        hall8a()
    elif direction == "s":
        hall9a()
    else:
        dead_end()
        hall9b()

def hall9c():
    logger.info('In hall 9c')
    
    tunnel()
    move_question()

    if direction == "n":
        hall9d()
    elif direction == "s":
        hall8a()
    else:
        dead_end()
        hall9c()

def hall9d():
    logger.info('In hall 9d')
    
    tunnel()
    move_question()

    if direction == "n":
        room6()
    elif direction == "s":
        hall9c()
    else:
        dead_end()
        hall9d()

def room6():
    logger.info('In room 6')
    
    room_description()
    r6action = input("Far in the corner you spot a dull object that looks out of place. What do you wish to do?")

    if r6action == "look object":
        print("You see an old key lying among the stones.")
        room6()
    elif r6action == "pickup key":
        character.Character.key = "true"
        
    move_question()

    if direction == "s":
        hall9d()
    else:
        dead_end()
        room6()

def hall7():
    logger.info('In hall 7')
    
    tunnel()
    move_question()

    if direction == "n":
        hall7a()
    elif direction == "s":
        room3()
    else:
        dead_end()
        hall7()

def hall7a():
    logger.info('In hall 7a')
    
    tunnel()
    move_question()

    if direction == "n":
        room5()
    elif direction == "s":
        hall7()
    else:
        dead_end()
        hall7a()

def room5():
    logger.info('In room 5')
    
    room_description()
    move_question()

    if direction == "s":
        hall7a()
    else:
        dead_end()
        room5()    


def hall5():
    logger.info('In hall 5')
    
    tunnel()
    move_question()

    if direction == "e":
        hall5a()
    elif direction == "w":
        hall3e()
    else:
        dead_end()
        hall5()

def hall5a():
    logger.info('In hall 5a')
    
    tunnel()
    move_question()

    if direction == "e":
        hall5b()
    elif direction == "w":
        hall5()
    else:
        dead_end()
        hall5a()

def hall5b():
    logger.info('In hall 5b')
    
    tunnel()
    move_question()

    if direction == "e":
        hall5c()
    elif direction == "w":
        hall5a()
    else:
        dead_end()
        hall5b()

def hall5c():
    logger.info('In hall 5c')
    
    tunnel()
    move_question()

    if direction == "n":
        hall5d()
    elif direction == "w":
        hall5b()
    else:
        dead_end()
        hall5c()

def hall5d():
    logger.info('In hall 5d')
    
    tunnel()
    move_question()

    if direction == "n":
        hall5c()
    elif direction == "s":
        hall5c()
    else:
        dead_end()
        hall5d()

def hall5e():
    logger.info('In hall 5e')
    tunnel()
    move_question()

    if direction == "s":
        hall5d()
    else:
        dead_end()
        hall5e()
