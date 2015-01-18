#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/entity.py
============================
This module houses the entity class. It is inherited by all
entitys in the game.
"""

class Entity:
    """
    Entity
    ======
    Represents an entity. Callable to update the entity's position.
    """

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        """update the position of the entity."""
        self.x, self.y = x, y

if __name__ == '__main__':
    pass
