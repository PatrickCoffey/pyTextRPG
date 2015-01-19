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
            
    def equipItem(self, item, slot):
        """Equips an item if there is currently one in inventory and it can be equipped"""
        if self.inventory._containsItem(item):
            iEquip = self.inventory.get(item.name)
            self.equipment._equipItem(item, slot)
            self.inventory._removeItem(iEquip, 1)
            return 'Equipped [' + item.name + '] to [' + slot + ']!'
        else:
            return 'Player does not have [' + item.name + '] to equip!'
    
    def unequipItem(self, slot):
        """Unequips item from slot if item equipped to slot and returns to inventory"""
        item = self.equipment[slot]
        if item != None:
            iUnequip = self.equipment._unequipItem(slot)
            self.inventory._addItem(iUnequip, 1)
            return 'Unequipped [' + item.name + '] from [' + slot + ']!'
        else:
            return 'Player does not have [' + item.name + '] equipped!'
            
    
    def getItem(self, container, item, quantity=1):
        """Get an Item from a container and add to characters inventory"""
        pass
    
    def putItem(self, container, item, quantity=1):
        """Put an Item from Characters inventory into container"""
        pass
            
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
        self.inventory._addItem(gold, 500)
        weapon1 = Weapon('Broken_Sword', 'The hilt of a broken sword')
        self.inventory._addItem(weapon1) 

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
