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
            if item.name == itemCheck.name:
                return True
        return False

        
class Inventory(Container):
    """
    Inventory:
    ==========
    This class represents a characters inventory, this holds items. 
    It is not the same as the Equipment class.
    It is inherited by all characters.
    """
    
    name = ''
    description = ''
    
    def __init__(self, name='Inventory', description='A collection of items'):
        Container.__init__(self, name)
        self.description = description
        
    def addItem(self, Item, Quantity):
        """Adds an item to the container"""
        if self._containsItem(Item):
            self[Item.name].quantity += Quantity
        else:
            self[Item.name] = Item
            self[Item.name].quantity = Quantity
            self[Item.name]._refresh()
    
    def removeItem(self, Item, Quantity):
        """Removes an item if in container"""
        if self._containsItem(Item):
            self[Item.name].quantity -= Quantity
            return Quantity + ' ' + Item.name + '\'s removed'
        else:
            return Item.name + ' is not in this container'    


class Equipment(Container):
    """
    Equipment:
    ==========
    This class represents a characters equipped items, this holds items. 
    It is not the same as the Equipment class.
    It is inherited by all characters.
    """
    
    name = ''
    description = ''
       
    
    def __init__(self, name='Equipment', description='Currently equipped items'):
        Container.__init__(self, name)
        self.description = description
        self['Helm'] = None
        self['Chest'] = None
        self['Legs'] = None
        self['Boots'] = None
        self['Gloves'] = None
        self['Left Hand'] = None
        self['Right Hand'] = None        

    def equipItem(self, item, slot):
        """equips new item and returns previous item from slot, None if nothing already equipped"""
        if self[slot] == None:
            self[slot] = item
            return None
        else:
            retItem = self[slot]
            self[slot] = item
            return retItem
        
    def unequipItem(self, slot):
        """Returns previous item from slot, None if nothing equipped"""
        if self[slot] == None:
            return None
        else:
            retItem = self[slot]
            return retItem 
        

if __name__ == '__main__':
    pass