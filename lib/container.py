#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/container.py
=========================
This module houses the inventory class. 
It is inherited by all characters.
"""

class Container(dict):
    """
    Container:
    ==============
    This is the base of the container class.
    It represents something which can hold items or entities.
    """
    
    name = ''
    
    def __init__(self, name='Container'):
        self.name = name
    
    def _containsItem(self, itemCheck):
        for item in self:
            if item == itemCheck:
                return True
        return False
            
    
    def addItem(self, Item, Quantity):
        """Adds an item to the container"""
        pass
    
    def removeItem(self, Item, Quantity):
        """Removes an item if in container"""
        pass

if __name__ == '__main__':
    pass