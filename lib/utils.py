#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/utils.py
============================
This module houses various utilities used throughout the game.
Most things that dont belong to a particular class type will be here.
"""

import commands as cmds
from container import *
from random import randint
from lib.items.armor import *
from lib.items.weapons import *
from lib.items.special import *
from lib.items.items import *
from lib.items.currency import *
from lib.items.potions import *
from lib.location import *

def inputText(prompt='What next?'):
    print(prompt)
    ret = raw_input('>> ')
    return ret

def inputCMD(prompt='What next?'):
    print(prompt)
    ret = raw_input('>> ')
    ret = ret.split()
    return list(ret)

def inputBool(prompt='Yes or No?'):
    print(prompt)
    while True:
        sInput = raw_input('>> ')
        sInput = sInput.lower()
        if sInput in ['y', 'yes', 'yeah', 'ok', 'agree']:
            return True
        elif sInput in ['n', 'no', 'nah', 'nope', 'negative']:
            return False

def getPlayerInfo():
    while True:
        sInput = inputText('What is your Name?')
        confirm = inputBool('So your name is ' + sInput.title() + '?')
        if confirm:
            return sInput
            
def parseInput(player, validCommands, *commands):
    """Parses and runs the given command if valid"""
    commands = list(commands)
    cmd = commands.pop(0)
    if cmd in validCommands.iterkeys():
        ret = validCommands[cmd](player, *commands)
        return ret
    elif cmd == 'god':
        return cmds.god()
        
def printCurrentItems(player):
    print('      ** ' + player.name + '\'s Items ** ')
    print('Equipment:')
    for slot, item in player.equipment.items():
        if item != None:
            print(' * [' + slot.capitalize() + '] - ' + item.name)
    print('Inventory:')
    for item in player.inventory.itervalues():
        if item != None:
            print(' * ' + item.name + ' x' + str(item.quantity))
    print('\n')     
        
def clearScreen():
    """Prints 1000 newlines to the terminal to clear screen"""
    pass
    #print('\n' * 100)
    
def randomChest():
    items = randomItems(1,10)
    chest = Chest(items)
    return chest

def randomItems(iMin, iMax):
    ret = []
    junk = ItemJunk
    while counter < iMax:
        rand = randint(1, 100)
        if rand < 80:
            ret.append(ItemJunk())
        elif rand < 90:
            if rand < 87:
                ret.append(Cleaver())
            else:
                ret.append(Pike())
        elif rand < 100:
            if rand < 93:
                ret.append(clothBoots())
            elif rand < 96:
                ret.append(clothChest())
            elif rand < 99:
                ret.append(clothLegs())
            elif rand == 99:
                ret.append(Buckler())
        else:
            ret.append(doublePluggers())
    

def printLocation(player):
    print(' ~ ' + player.location.name + ' ~ ')
    print(player.location.description)