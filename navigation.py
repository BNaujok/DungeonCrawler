# Currently this is the navigation file for the dungeon.
# 9/2/2017 dungeon is at a single level with varied length halls in which you can travel in either direction using cardinal points
# Need random item/encounter functionality to be built into the program.

import character 

def entrance():
    print("You are standing at the entrance of a cavern. You see doors leading out of the room to the North, East and West.")
    d = input("Which direction will you head? enter the letter that represents the direction you wish to go")

    if d == "n":
        hall3_north()
    elif d == "w":
        hall2_west()
    elif d == "e":
        hall1_east()
    else:
        print("Please enter n, e or w for your movement.")
        entrance()

def hall1_east():
    print("You are in a dark corridor heading east. You can see the faint glimmer of a chamber ahead.")
    d = input("Which way will you head?")

    if d == "e":
        hall1a_east()
    elif d == "w":
        entrance()
    else:
        print("You see a wall")
        hall1_east()
        
        
def hall1a_east():
    print("You are still in a corridor, the light is much brighter now.")
    d = input("Which way will you head?")

    if d == "e":
        room1()
    elif d == "w":
        hall1_west()
    else:
        print("You see a wall")
        hall1a_east()

def hall1a_west():
    print("You are in a dark corridor heading west. You can see the faint glimmer of a chamber ahead.")
    d = input("Which way will you head?")

    if d == "e":
        room1()
    elif d == "w":
        hall1_west()
    else:
        print("You see a wall")
        hall1a_west()

def hall1_west():
    print("You are still in a corridor, the light is much brighter now.")
    d = input("Which way will you head?")

    if d == "e":
        hall1a_east()
    elif d == "w":
        entrance()
    else:
        print("You see a wall")
        hall1_west()

def room1():
    print("You have entered a bright cavern. There is the glimmer of an object on the floor nearby.")
    print("There are no other exits other than the one you just came through")
    d = input("What do you wish to do?")

    if d == "w":
        hall1a_west()
    elif d == "look":
        o = input("There is a knife lying on the ground. What would you like to do?")

        if o == "pickup knife":
            character.character.bag.append("knife")
            print("the knife has been placed into your bag")
 
        else:
            room1()

    elif d == "e" or "n" or "s":
        print("You encounter the edge of the room")
        room1()

    else:
        print("That is not a valid command")
        room1()

def hall2_west():

    print("You are in a dark corridor heading west. You can't see much beyond the torch light around you.")
    d = input("Which way will you head?")

    if d == "e":
        entrance()
    elif d == "w":
        hall2a_west()
    else:
        print("You bump into a wall")
        hall2_west()
    
def hall2_east():

    print("You are in a dark corridor heading east. You can see the entrance lying before you")
    d = input("Which way will you head?")

    if d == "e":
        entrance()
    elif d == "w":
        hall2a_west()
    else:
        print("You bump into a wall")
        hall2_east()
                  
def hall2a_west():

    print("You are in a dark corridor heading west. You can't see much beyond the torch light around you.")
    d = input("Which way will you head?")

    if d == "e":
        hall2_east()
    elif d == "w":
        hall2b()
    else:
        print("You bump into a wall")
        hall2a_west()

def hall2a_east():

    print("You are in a dark corridor heading east. You can't see much beyond the torch light around you.")
    d = input("Which way will you head?")

    if d == "e":
        hall2_east()
    elif d == "w":
        hall2b()
    else:
        print("You bump into a wall")
        hall2a_east()

def hall2b():

    print("You are in a dark corridor heading west. You can't see much beyond the torch light around you.")
    d = input("Which way will you head?")

    if d == "e":
        hall2a_east()

    else:
        print("You have encountered a dead end.")
        hall2b()
