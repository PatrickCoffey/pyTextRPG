#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/items/weapons.py
================================
This module houses the types of general weapons in the game. 
"""

from ..item import Weapon


class BrokenSword(Weapon):
    """This is the starting item"""
    
    def __init__(self, name='Broken_Sword', description='The hilt of a broken sword'):
        Weapon.__init__(self, name, description, 0, 1, [0,1])
        self.slot.append('Left_Hand')
        self.slot.append('Right_Hand')