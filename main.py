#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - main.py
============================
This is the main loop for the game.
"""

from lib.utils import *
from lib.player import Player

def main():
    while True:
        playerName = getPlayerInfo()
        player = Player(playerName)
        

if __name__ == "__main__":
    main()