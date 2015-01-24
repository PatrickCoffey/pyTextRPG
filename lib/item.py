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
    lowName = ''
    description = ''
    quantity = 1
    owner = None
    type = []
    
    
    def __init__(self, name='Thing', description='a thing', value=1, quantity=1):
        self.name = name
        self.lowName = name.lower().replace(' ', '_')
        self.description = description
        self.value = value
        self.quantity = quantity
        self.type.append('Item')
        self._refresh()
    
    def __str__(self):
        return self.lowName
    
    def _refresh(self):
        self.netValue = (self.value * self.quantity)
        
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
    
    slot =[]
    
    def __init__(self, name='Blade', description='a small blade', value=1, quantity=1, damage=[1,1]):
        Item.__init__(self, name, description, value, quantity)
        self.damageMin = damage[0]
        self.damageMax = damage[1]
        self.type.append('Weapon')
        
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
    
    slot =[]

    def __init__(self, name='cloth', description='a tattered cloth', value=1, quantity=1, armor=0):
        Item.__init__(self, name, description, value, quantity)
        self.armor = armor
        self.type.append('Armor')
       
class Currency(Item):
    """
    Currency:
    =========
    Everyone knows what currency is. (eg. gold)
    """
    
    def __init__(self, name='Gold', description='Gold Pieces', value=1, quantity=1):
        Item.__init__(self, name, description, value, quantity)
        self.type.append('Currency')

class ItemJunk(Item):
    """
    ItemJunk:
    =========
    This represents stuff you sell for money.
    Its entirely useless for any other purpose.
    """
    
    def __init__(self, name='Junk', description='Useless junk!', value=1, quantity=1):
        Item.__init__(self, name, description, value, quantity)

if __name__ == '__main__':
    pass