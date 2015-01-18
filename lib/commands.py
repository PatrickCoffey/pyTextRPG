#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/commands.py
===========================
This module holds all the various commands that the user can execute.
"""

import sys

def help(player):
    """Shows available commands"""
    print('This is the help menu')
    for command in Commands.iterkeys():
        print(" * " + command)
    print('\n')
    
    
def inv(player):
    """Shows the inventory of current player"""
    print('Equipment:')
    for slot, item in player.equipment.items():
        if item != None:
            print(' * [' + slot.capitalize() + '] - ' + item.name)
    print('Inventory:')
    for item in player.inventory.itervalues():
        if item != None:
            print(' * ' + item.name + ' x' + str(item.quantity))
    print('\n')
        
        
def confront(player, character):
    pass


def exit(player):
    sys.exit()
        
Commands = {'help': help,
            'inv' : inv,
            'confront': confront,
            'exit': exit
}