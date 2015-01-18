#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/item.py
=========================
This module houses the item class. 
It represents an object. 
Most non entities inherit from this.
"""

import random

class Item(object):
    """
    Item:
    =====
    This is the base of the games Items.
    It represents an object.
    Most non entities inherit from this.
    """
    
    name = ''
    description = ''
    quantity = 1
    owner = None
    
    
    def __init__(self, name='Thing', description='a thing', value=1, quantity=1, owner=None):
        self.name = name
        self.description = description
        self.value = value
        self.quantity = quantity
        self.owner = owner
        self._refresh()     
    
    def _refresh(self, owner=None):
        self.netValue = (self.value * self.quantity)
        if owner != None:
            self.owner = owner
        
    def _checkQuant(self, quantity):
        if self.quantity >= quantity:
            return True
        else:
            return False
        

class Weapon(Item):
    """
    Item:
    =====
    This is the base of the games Items.
    It represents an object.
    Most non entities inherit from this.
    """
    
    name = ''
    description = ''
    quantity = 1
    
    
    def __init__(self, name='Blade', description='a small blade', value=1, quantity=1, damage=[1,1]):
        Item.__init__(self, name, description, value, quantity)
        self.damageMin = damage[0]
        self.damageMax = damage[1]
        
    def _calcDamage(self, character):
        dmg = random.randint(self.damageMin, self.damageMax) - character.armor
        if dmg <= 0:
            return 0
        else:
            return dmg        


class Armor(Item):
    """
    Item:
    =====
    This is the base of the games Items.
    It represents an object.
    Most non entities inherit from this.
    """

    def __init__(self, name='cloth', description='a tattered cloth', value=1, quantity=1, armor=0):
        Item.__init__(self, name, description, value, quantity)
        self.armor = armor

       
class Gold(Item):
    """
    Gold:
    =====
    Everyone knows what gold is. eg. currency
    """
    def __init__(self):
        Item.__init__(self, 'Gold', 'Gold Coins')

if __name__ == '__main__':
    pass