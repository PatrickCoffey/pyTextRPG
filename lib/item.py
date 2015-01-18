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
    
    def __init__(self, name='Container'):
        self.name = name

if __name__ == '__main__':
    pass