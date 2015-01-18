#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/utils.py
============================
This module houses various utilities used throughout the game.
Most things that dont belong to a particular class type will be here.
"""


def inputText(prompt='What next?'):
    print(prompt)
    ret = raw_input('>> ')
    return ret

def inputCMD(prompt='What next?'):
    print(prompt)
    ret = raw_input('>> ')
    ret = ret.split()
    return ret

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
            
def parseInput(player, command, validCommands):
    """Parses and runs the given command if valid"""
    cmd = command.pop(0)
    if cmd in validCommands.iterkeys():
        ret = validCommands[cmd](player, *command)
        return ret
        
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
    print('\n' * 100)