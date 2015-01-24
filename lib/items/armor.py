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
        Armor.__init__(self, name, description, value, quantity, armor)
        self.armor = armor
        self.slot.append('Chest')
        
        
class clothLegs(Armor):
    """
    clothLegs:
    ==========
    This is the starting armor.
    """
    
    def __init__(self, name='Cloth (legs)', description='a tattered cloth', value=1, quantity=1, armor=0):
        Armor.__init__(self, name, description, value, quantity, armor)
        self.slot.append('Legs')
        
        
class clothBoots(Armor):
    """
    clothBoots:
    ==========
    This is the starting armor.
    """
    
    def __init__(self, name='Cloth Boots', description='a pair or clothes to wrap around feet', value=1, quantity=1, armor=0):
        Armor.__init__(self, name, description, value, quantity, armor)
        self.slot.append('Boots')
        

class Buckler(Armor):
    """
    Buckler:
    ========
    This is the most basic shield.
    """
    
    def __init__(self, name='Buckler', description='A small shield', value=1, quantity=1, armor=0):
        Armor.__init__(self, name, description, value, quantity, armor)
        self.slot.append('Left_Hand')
        self.slot.append('Right_Hand')
        