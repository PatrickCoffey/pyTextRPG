#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/items/armor.py
==============================
This module houses the types of armor in the game. 
"""

from ..item import Armor

class clothChest(Armor):
    """
    clothChest:
    ===========
    This is the starting armor.
    """

    def __init__(self, name='Cloth (chest)', description='a tattered cloth', value=1, quantity=1, armor=0):
        Item.__init__(self, name, description, value, quantity)
        self.armor = armor
        self.type = 'Armor'
        self.slot = 'Chest'
        
class clothLegs(Armor):
    """
    clothLegs:
    ==========
    This is the starting armor.
    """

    def __init__(self, name='Cloth (legs)', description='a tattered cloth', value=1, quantity=1, armor=0):
        Item.__init__(self, name, description, value, quantity)
        self.armor = armor
        self.type = 'Armor'
        self.slot = 'Legs'
        