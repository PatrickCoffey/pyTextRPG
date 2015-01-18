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
            
def parseInput(player, sInput, Commands):
    """Parses and runs the given command if valid"""
    if sInput in Commands.iterkeys():
        Commands[sInput](player)