# D&D style dungeon crawler that initially is text based.

# This will be the main file into which each of the separate modules can interact.
# Currently the navigation file is already getting large and only two corridors and rooms have been added into it.
# Object classes need to be created for the character as well as a few monsters for random encounters
# A bag array needs to be established to assist the character to get through set puzzles throughout the dungeon.

import character
import navigation
import logging

character.Character.knife = "false"
character.Character.key = "false"

# setting logging level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


logger.info('Entering the dungeon')

navigation.entrance()

