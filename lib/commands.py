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
    return 'confront'

def go(player, *args):
    pass

def search(player, *args):
    if str(args[0]).lower() == 'room':
        ret = searchRoom(player)
        return ret
    for conName, container in player.location.containers.iteritems():
        if str(args[0]).lower() == conName.lower():
            return container
            

def searchRoom(player):
    ret = "You look around...\n"
    ret += "  Containers:\n"
    if player.location.containers != None:
        for container in player.location.containers:
            ret += "  - " + container + "\n"
        ret += "\n"
    else:
        ret += "    None\n"
        ret += "\n"
    ret += "  Enemies:\n"
    if player.location.enemies != {}:
        for enemy in player.location.enemies:
            ret += "  - " + enemy.name + "\n"
        ret += "\n"
    else:
        ret += "    None\n"
        ret += "\n"
    return ret

def exit(player, *args):
    sys.exit()
        
Commands = {'help': help,
            'inv' : inv,
            'search': search,
            'confront': confront,
            'go' : go,
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

def conHelp(player, *args):
    pass

def get(player, *args):
    """Shows available commands"""
    if len(args) == 2:
        if player.location.containers != None:
            for container in player.location.containers:
                if str(args[0]).lower() == container.name.lower():
                    conFrom = container
                    break
                else:
                    return "No container named " + str(args[0]) + " in this room"
            for itemName, item in conFrom.iteritems():
                if str(args[1]).lower() == str(itemName).lower():
                    grabbedItem = item
                    conFrom._removeItem(item)
                    player.inventory._addItem(grabbedItem)
                else:
                    return "No item named " + str(args[1]) + " in " + str(args[0])
    else:
        return "Invalid Syntax"

#def put(player, *args):
    #"""Shows available commands"""
    #pass

conCommands = {'help': conHelp,
               'show': show,
               'get' : get,
               #'put' : put,
               'back': back,
               'exit': exit
}