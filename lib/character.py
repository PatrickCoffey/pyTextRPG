#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
pyTextRPG - lib/character.py
============================
This module houses the character classes.
"""

from container import *
from items.currency import *
from items.weapons import *
from items.armor import *
from items.potions import *
from items.special import *
from items.items import *

class CharacterBase(object):
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
        self.location = None
    
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
            iEquip = None
            for itemCheck in self.inventory.values():
                if itemCheck.lowName == item:
                    iEquip = itemCheck
                    self.inventory._removeItem(itemCheck)
            equipRet = self.equipment._equipItem(iEquip, slot)
            if isinstance(equipRet, str):
                return equipRet
            if isinstance(equipRet, Item):
                self.inventory._addItem(equipRet)
            self._refreshEquip()
            return 'Equipped "' + item + '" to [' + slot + ']!'
        else:
            return 'Player does not have a "' + item + '" to equip!'
    
    def unequipItem(self, slot):
        """Unequips item from slot if item equipped to slot and returns to inventory"""
        item = self.equipment[slot]
        if item != None:
            iUnequip = self.equipment._unequipItem(slot)
            self.inventory._addItem(iUnequip, 1)
            self._refreshEquip()
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
        val = 0
        for item in self.equipment.values():
            if item != None:
                if 'Armor' in item.type:
                    val += item.armor
        self.armor = val
    
    def _calcDamage(self):
        valMax = 0
        valMin = 0
        for item in self.equipment.values():
            if item != None:
                if 'Weapon' in item.type:
                    valMin += item.damageMin
                    valMax += item.damageMax
        self.damageMin = valMin + self.baseDamage
        self.damageMax = valMax + self.baseDamage
        
class Player(CharacterBase):
    """
    Player:
    =======
    This is the players character.
    It inherits character base like all characters in the game.
    """
    _xpForLvl = {1: 50,
                 2: 100,
                 3: 200,
                 4: 400,
                 5: 800}
    
    def __init__(self, name='Player', health=10, description='A renowned hero!', baseDamage=0, baseArmor=0):
        CharacterBase.__init__(self, name, health)
        self.description = description
        self.xp = 0
        self.lvl = 0
        self._startItems()
        self._refreshEquip()
        
    def _startItems(self):
        self.inventory._addItem(Gold(quantity=500))
        self.inventory._addItem(BrokenSword())
        #self.inventory._addItem(Cleaver())
        
    def _updateLvl(self):
        for possibleLvl, xpNeeded in self._xpForLvl():
            if self.xp < xpNeeded:
                lvl = possibleLvl - 1
                self.baseArmor = lvl
                self.baseDamage = lvl
                

class Enemy(CharacterBase):
    """
    Enemy:
    ======
    This is the enemy class.
    It inherits character base like all characters in the game.
    """
    
    xpGain = 0
    
    def __init__(self, name='default', health=1, typeName='default', description='default', baseDamage=0, baseArmor=0, xpGain=10):
        CharacterBase.__init__(self, name, health)
        self.typeName = typeName
        self.description = description


if __name__ == '__main__':
    pass
