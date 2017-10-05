# 23/4/17 Monster random encounter module
# Sets up the possibility of a random encounter
# Creates a random fight sequence once a weapon has been established with the character
# 5/10/17 Created a random encounter sequence to enable different monsters to spawn. Created a HP tracker to enable us to know when the monster has been defeated and a return to previous module

import character
import random
import logging

# setting logging level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# a list of random monsters for encounters after retrieving the knife
mon_list = ['rat', 'wolf', 'blob', 'goblin', 'snake']
mon_HP = [8, 15, 12, 25, 9]

def random_encounter():
# establishes whether an encounter is to take place, and if so, with which monster
    d4_roll = random.randint(1, 4)
    logging.debug('d4_roll %s', d4_roll)
    if d4_roll == 4:

        randomindex = random.randint(0,len(mon_list)-1)  
        logging.debug('%s', randomindex)
        
        generate_monster(mon_list[randomindex], mon_HP[randomindex])
        fight_sequence()


def generate_monster(name, HP):
# establishes the parameters of the monster for the fight
    character.Monster.name = name
    character.Monster.HP = HP
    
    print("You have encountered a ", character.Monster.name, ".")

def fight_sequence():
# tracks the progress of the monster as it loses its HP    
    while character.Monster.HP > 0:
        d6_roll = random.randint(1, 6)
        print('You deal ', d6_roll, ' damage.')
        character.Monster.HP = character.Monster.HP - d6_roll
        

    print(character.Monster.name, " has been defeated!")
        
