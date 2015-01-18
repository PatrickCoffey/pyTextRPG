#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/entity.py
============================
This module houses the entity class. It is inherited by all
entities in the game.
"""

class Entity(object):
    """
    Entity
    ======
    Represents an entity. Callable to update the entity's position.
    """

    location = object
    
    def __init__(self, location):
        self.location = location

    def __call__(self, location):
        """update the position of the entity."""
        self.location = location
     

if __name__ == '__main__':
    pass
