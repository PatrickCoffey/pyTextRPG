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

def god():
    return 'god'
    
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
    if len(args) == 2:
        if str(args[1]).lower() in str(player.equipment.keys()).lower():
            ret = player.equipItem(*args)
            return ret
        else:
            return 'derp'
    else:
        return "Invalid Syntax"  

def unequip(player, *args):
    """Shows available commands"""
    if len(args) == 1:
        if str(args[0]).lower() in str(player.equipment.keys()).lower():
            ret = player.unequipItem(args[0])
            return ret
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