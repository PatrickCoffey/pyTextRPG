#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/items/weapons.py
================================
This module houses the types of general weapons in the game. 
"""

from ..item import Weapon


class BrokenSword(Weapon):
    """
    BrokenSword:
    ============
    This is the starting weapon, its shit.
    """
    
    def __init__(self, name='Broken_Sword', description='The hilt of a broken sword'):
        Weapon.__init__(self, name, description, 0, 1, [1,1])
        self.slot.append('Left_Hand')
        self.slot.append('Right_Hand')
        
class Cleaver(Weapon):
    """
    Cleaver:
    ========
    This is a rusty cleaver, its pretty unreliable.
    """
    
    def __init__(self, name='Rusty Cleaver', description='An old rusty meat cleaver!'):
        Weapon.__init__(self, name, description, 50, 1, [0,5])
        self.slot.append('Left_Hand')
        self.slot.append('Right_Hand')
        
class Pike(Weapon):
    """
    Pike:
    =====
    This is a long pike, its unreliable.
    """
    
    def __init__(self, name='Pike', description='An unreliable but long pike!'):
        Weapon.__init__(self, name, description, 80, 1, [0,7])
        self.slot.append('Left_Hand')
        self.slot.append('Right_Hand')