#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/character.py
============================
This module houses the character classes.
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
    dead = False
    armor = 0
    
    def __init__(self, name='default', health=1):
        self.name = name
        self.health = health
        self.dead = False

        
class Player(CharacterBase):
    """
    Player:
    =======
    This is the players character.
    It inherits character base like all characters in the game.
    """
    
    name = ''
    health = 0
    description = ''
    
    def __init__(self, name='Player', health=10, description='A renowned hero!'):
        CharacterBase.__init__(self, name, health)
        self.description = description

class Enemy(CharacterBase):
    """
    enemy:
    ======
    This is the enemy class.
    It inherits character base like all characters in the game.
    """
    
    name = ''
    health = 0
    typeName = ''
    description = ''
    
    def __init__(self, name='default', health=1, typeName='default', description='default'):
        CharacterBase.__init__(self, name, health)
        self.typeName = typeName
        self.description = description

if __name__ == '__main__':
    pass
