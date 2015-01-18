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

def inInventory():
    pass


def inBattle():
    pass

def main():
    playerName = getPlayerInfo()
    player = Player(playerName)    
    while True:
        sInput = inputText()
        parseInput(player, sInput, Commands)

if __name__ == "__main__":
    main()