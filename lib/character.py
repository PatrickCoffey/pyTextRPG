#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/character.py
============================
This module houses the character base class. It is inherited by all
characters in the game.
"""
from entity import Entity

class CharacterBase(Entity):
    """
    characterBase:
    ==============
    This is the base of the character class.
    """
    
    name = ''
    health = 0
    
    def __init__(self, name='default', health=1):
        self.name = name
        self.health = health

if __name__ == '__main__':
    pass
