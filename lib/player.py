#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/player.py
=========================
This module houses the player's class. It inherits character base
like all characters in the game.
"""

from character import CharacterBase

class Player(CharacterBase):
    """
    characterBase:
    ==============
    This is the base of the character class.
    """
    
    name = ''
    health = 0
    description = ''
    
    def __init__(self, name='Player', health=10, description='A renowned hero!'):
        CharacterBase.__init__(self, name, health)
        self.description = description
        

if __name__ == '__main__':
    pass
