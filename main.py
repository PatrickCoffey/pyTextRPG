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
from lib.items.armor import *
from lib.items.weapons import *
from lib.items.special import *
from lib.items.items import *
from lib.items.currency import *
from lib.items.potions import *
from lib.location import *

def inGodMenu(player):
    clearScreen()
    printCurrentItems(player)
    while True:
        sInput = inputCMD()
        ret = parseInput(player, invCommands, sInput)
        if ret == 'back':
            break
        elif ret == 'show':
            printCurrentItems(player)  
        else:
            print(ret)

def inInventory(player):
    clearScreen()
    printCurrentItems(player)
    while True:
        sInput = list(inputCMD('(inv) What Next?'))
        ret = parseInput(player, invCommands, *sInput)
        if ret == 'back':
            break
        elif ret == 'show':
            printCurrentItems(player)  
        else:
            print(ret)

def inBattle(player):
    clearScreen()
    print('Entering Battle...')
    while True:
        pass


def main():
    playerName = getPlayerInfo()
    player = Player(playerName)
    player.location = Location(containers={'Chest': randomChest()})
    while True:
        printLocation(player)
        command = inputCMD()
        ret = parseInput(player, Commands, *command)
        
        if ret == "inv":
            inInventory(player)
        if ret == "god":
            inGodMenu(player)
        if ret == "confront":
            inBattle(player)
        

if __name__ == "__main__":
    main()