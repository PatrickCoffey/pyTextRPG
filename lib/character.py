#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/character.py
============================
This module houses the character classes.
"""

from entity import Entity
from container import Inventory, Equipment
from item import Weapon, Gold

class CharacterBase(Entity):
    """
    characterBase:
    ==============
    This is the base of the character class.
    """
    
    def __init__(self, name='default', health=1, baseDamage=0, baseArmor=0):
        self.name = name
        self.health = health
        self.dead = False
        self.armor = 0
        self.damage = 0
        self.inventory = Inventory(description=self.name + '\'s Inventory')
        self.equipment = Equipment(description=self.name + '\'s Equipment')
        self.baseDamage = baseDamage
        self.baseArmor = baseArmor
    
    def _attack(self, character):
        damage = self._calcDamage(character)
        life = character.health - damage
        if life <= 0:
            character.dead = true
            character.health = 0
        else:
            character.health = life
            
    def _refreshEquip(self):
        self._calcArmor()
        self._calcDamage()
        
    def _calcArmor(self):
        pass
    
    def _calcDamage(self):
        pass
        
class Player(CharacterBase):
    """
    Player:
    =======
    This is the players character.
    It inherits character base like all characters in the game.
    """
        
    def __init__(self, name='Player', health=10, description='A renowned hero!', baseDamage=0, baseArmor=0):
        CharacterBase.__init__(self, name, health)
        self.description = description
        self._startItems()
        self._refreshEquip()
        
    def _startItems(self):
        gold = Gold()
        self.inventory.addItem(gold, 500)
        weapon1 = Weapon('Broken Sword', 'The hilt of a broken sword')
        self.equipment.equipItem(weapon1, 'Right Hand')       

class Enemy(CharacterBase):
    """
    Enemy:
    ======
    This is the enemy class.
    It inherits character base like all characters in the game.
    """
    
    def __init__(self, name='default', health=1, typeName='default', description='default', baseDamage=0, baseArmor=0):
        CharacterBase.__init__(self, name, health)
        self.typeName = typeName
        self.description = description


if __name__ == '__main__':
    pass
