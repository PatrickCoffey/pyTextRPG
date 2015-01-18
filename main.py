#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - main.py
============================
This is the main loop for the game.
"""

from lib.utils import *
from lib.character import *
from lib.commands import *
from lib.container import *
from lib.item import *

def inInventory(player):
    clearScreen()
    printCurrentItems(player)
    while True:
        sInput = inputCMD()
        ret = parseInput(player, sInput, invCommands)
        if ret == 'back':
            break
        elif ret == 'show':
            printCurrentItems(player)  
        else:
            print(ret)

def inBattle():
    clearScreen()
    print('Entering Battle...')
    while True:
        pass


def main():
    playerName = getPlayerInfo()
    player = Player(playerName)    
    while True:
        command = inputCMD()
        ret = parseInput(player, command, Commands)
        
        if ret == "inv":
            inInventory(player)
        

if __name__ == "__main__":
    main()