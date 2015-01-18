#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/enemy.py
========================
This module houses the enemy's class. It inherits character base
like all characters in the game.
"""

from character import CharacterBase

class Enemy(CharacterBase):
    """
    enemy:
    ======
    This is the enemy class.
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
