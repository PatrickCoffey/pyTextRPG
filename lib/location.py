#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/location.py
===========================
This module houses the location class.
"""

obstructions = ['a Wall', 'a pile Rubble', 'a large Statue', 'an Animal Carcass']

class Location(object):
    """
    Location:
    =========
    This represents a location in the game, you can possibly travel N,S,E,W
    It can contain enemies, Containers, or a mixture
    """
    
    name = ''
    description = ''
    enemies = []
    containers = {}
    hidden = {}
    
    north = None
    east = None
    south = None
    west = None
    
    def __init__(self, name='A Dim Room', description='Its dark in here, I can barely see', enemies={}, containers={}, hidden={}):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.containers = containers
        self.hidden = hidden
        self._updateNeighbours()
        
    def __str__(self):
        return ' # ' + self.name + ' # \n' + self.description
    
    def __repr__(self):
        return self.name.lower().replace(' ', '_')
    
    def _updateNeighbours(self, north=None, east=None, south=None, west=None):
        """for a dead end pass the name of the obstruction eg. 'rubble' or 'wall'"""
        if north != None:
            self.north = north
        if east != None:
            self.east = east
        if south != None:
            self.south = south
        if west != None:
            self.west = west
            
