#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/items/special.py
================================
This module houses the types of special items in the game.
"""


from ..item import *

class doublePluggers(Armor, Weapon):
    """
    doublePluggers:
    ===============
    Get a slice of 'STRAYA up ya!
    """

    def __init__(self, name='Double Pluggers', description='\'STRAYA!', value=1000, quantity=1, armor=0):
        Armor.__init__(self, name, description, value, quantity, 3)
        Weapon.__init__(self, name, description, value, quantity, [1,25])
        self.type = ['Armor, Weapon']
        self.slot = ['Boots', 'Left_Hand', 'Right_Hand']
        