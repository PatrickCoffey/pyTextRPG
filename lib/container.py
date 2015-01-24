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
    ==========
    This is the base of the container class.
    It represents something which can hold items or entities.
    """
    
    name = ''
    
    def __init__(self, name='Container'):
        self.name = name
    
    def _containsItem(self, itemCheck):
        if str(itemCheck).lower() in str(self.keys()).lower():
                return True
        return False
    
    def _listItems(self):
        ret = ''
        for item in self.keys():
            ret = item + '\n'
        return ret
    
    def _addItem(self, Item):
        """Adds an item to the container"""
        if self._containsItem(Item):
            self[Item.name].quantity += Item.quantity
        else:
            self[Item.name] = Item
            self[Item.name]._refresh()
    
    def _removeItem(self, Item, quantity=1):
        """Removes an item if in container"""
        if self._containsItem(Item):
            if self[Item.name].quantity <= quantity:
                del self[Item.name]
            else:
                self[Item.name].quantity -= quantity
        else:
            return Item.name + ' is not in this container'     

        
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
        self['helm'] = None
        self['chest'] = None
        self['legs'] = None
        self['boots'] = None
        self['gloves'] = None
        self['left_hand'] = None
        self['right_hand'] = None        

    def _equipItem(self, item, slot):
        """equips new item and returns previous item from slot, None if nothing already equipped"""
        
        if not str(slot).lower() in str(item.slot).lower():
            return "I can't put that there!"
        if self[slot] == None:
            self[slot] = item
            return None
        else:
            retItem = self[slot]
            self[slot] = item
            return retItem
        
    def _unequipItem(self, slot):
        """Returns previous item from slot, None if nothing equipped"""
        if self[slot] == None:
            return None
        else:
            retItem = self[slot]
            self[slot] = None
            return retItem 
        
class Chest(Container):
    """
    Chest:
    ======
    This is a chest, it holds items and gold etc...
    """
    
    def __init__(self, *contents):
        if contents != None:
            for item in contents:
                self._addItem(item)
        
    
if __name__ == '__main__':
    pass