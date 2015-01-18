#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/inventory.py
=========================
This module houses the inventory class. 
It is inherited by all characters.
"""

from container import Container

class Inventory(Container):
    """
    characterBase:
    ==============
    This is the base of the character class.
    """
    
    name = ''
    description = ''
    
    def __init__(self, name='Inventory', description='A collection of items'):
        Container.__init__(self, name)
        self.description = description

    
    
        

if __name__ == '__main__':
    pass
