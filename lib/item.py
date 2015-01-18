#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/item.py
=========================
This module houses the item class. 
It represents an object. 
Most non entities inherit from this.
"""

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
    
    
    def __init__(self, name='Thing', description='a thing', value=1, quantity=1):
        self.name = name
        self.description = description
        self.value = value
        self.quantity = quantity
        self._refresh()
    
    def _refresh(self):
        self.netValue = (self.value * self.quantity)
        
    def _checkQuant(self, quantity):
        if self.quantity >= quantity:
            return True
        else:
            return False

if __name__ == '__main__':
    pass