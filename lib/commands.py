#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/commands.py
===========================
This module holds all the various commands that the user can execute.
"""

import sys

def help(player, *args):
    """Shows available commands"""
    print('This is the help menu')
    for command in Commands.iterkeys():
        print(" * " + command)
    print('\n')
    
    
def inv(player, *args):
    """Shows the inventory of current player"""
    return 'inv'
        
        
def confront(player, *args):
    pass


def exit(player, *args):
    sys.exit()
        
Commands = {'help': help,
            'inv' : inv,
            'confront': confront,
            'exit': exit
}

def invHelp(player, *args):
    """Shows available commands"""
    print('This is the help menu')
    for command in invCommands.iterkeys():
        print(" * " + command)
    print('\n')
    
def equip(player, *args):
    """Shows available commands"""
    if args.count == 2:
        if str(args[0]).lower() in player.equipment.iterKeys():
            retItem = player.equipment._equipItem(args[1])
            player.inventory.addItem(retItem, retItem.quantity)
            return args[0] + " unequipped!"
    else:
        return "Invalid Syntax"    

def unequip(player, *args):
    """Shows available commands"""
    if args.count == 2:
        if str(args[0]).lower() == 'slot':
            retItem = player.equipment.unequipItem(args[1])
            player.inventory.addItem(retItem, retItem.quantity)
            return args[0] + " unequipped!"
    else:
        return "Invalid Syntax"

def back(player, *args):
    """Shows available commands"""
    return('back')

def show(player, *args):
    """Shows available commands"""
    return('show')

invCommands = {'help': invHelp,
               'show': show,
               'equip' : equip,
               'unequip' : unequip,
               'back': back,
               'exit': exit
}