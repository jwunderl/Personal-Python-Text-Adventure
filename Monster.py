import random
import Weapon
from Shared import *

class Monster(Character):
	difficulty_level = ("easy", "normal", "exceptional")

	def __init__(self, name, level = 1, difficulty = 1):
		self.name = name
		self.difficulty = difficulty
		self.level = level
		self.alive = True
		self.equipped_weapon = None
		self.experience = 0

	def deal_damage(self, damage):
		return super(Monster, self).deal_damage(damage, "attacking the dead creature has no effect")

	def level_up(self):
		super(Monster, self).level_up(False)

	def give_exp(self, amount):
		super(Monster, self).give_exp(amount, False)

	def __repr__(self):
		return (self.class_name + "(" + self.name + ", " + 
						self.level + ", " + self.difficulty + ")")

	def __str__(self):
		return self.name + " the " + self.class_name.lower()

	def display_inventory(self):
		super(Monster, self).display_inventory(False)

	def equip_item(self):
		super(Monster, self).equip_item()

class Goblin(Monster):
	class_name = "Goblin"
	desc = "\ta fairly weak mischievous, ugly, dwarflike creature"
	aptitude = ("\tincapable of using magic, this type of monster"
				+" also renders magic near useless against themselves")
	level_modifier = { 	# modifiers applied on level
		"health"		: 1.04,
		"attack"		: 1.05,
		"endurance"		: 1.02,
		"vitality"		: 1.08,
		"mana"			: 1,
		"movement speed": 1.04,
		"intellect"		: 1
	}

	def __init__(self, name, level = 1, difficulty = 1):
		super(Goblin, self).__init__(name, level, difficulty)
		self.modifiers = {		# modifiers for equipment
			"melee"				: .8,
			"melee defense"		: .75,
			"ranged"			: .8,
			"ranged defense"	: .75,
			"magic"				: 0,
			"defense"			: 1,
			"magic defense"		: 1.5,
			"fire resistance"	: .75,
			"ice resistance"	: .75,
			"speed"				: 1.2
		}

		self.statistics_base = {
			"health"		: 65 +  (15 * difficulty),
			"attack"		: 30 +  (10 * difficulty),
			"endurance"		: 80 +  (20 * difficulty),
			"vitality"		: 60 +  (8 * difficulty),
			"mana"			: 0,
			"movement speed": 90 +  (15 * difficulty),
			"intellect"		: 0
		}

		self.statistics = dict()
		for key in self.statistics_base:
			self.statistics_base[key] = (self.statistics_base[key]
									* (self.level_modifier[key] ** level))
		self.current_health = self.statistics_base["health"]
		self.current_mana = self.statistics_base["mana"]

		self.inventory = list()
		sword = Weapon.LongSword(1, 2, True)
		self.inventory.append(sword)
		self.equipped_weapon = sword
		self.drops = {
			"experience" 	: 45 * level,
			"gold"			: 25 * level,
			"items"			: self.inventory
		}

class Dragon(Monster):
	class_name = "Dragon"
	desc = "\ta large conglomeration of a snake and a serpent"
	aptitude = ("\tGreatly resitant to fire")
	level_modifier = { 	# modifiers applied on level
		"health"		: 1.04,
		"attack"		: 1.1,
		"endurance"		: 1.02,
		"vitality"		: 1.08,
		"mana"			: 1,
		"movement speed": 1.04,
		"intellect"		: 1
	}

	def __init__(self, name, level = 1, difficulty = 1):
		super(Dragon, self).__init__(name, level, difficulty)
		self.modifiers = {		# modifiers for equipment
			"melee"				: 1.2,
			"melee defense"		: 1.1,
			"ranged"			: 1.2,
			"ranged defense"	: 1.0,
			"magic"				: 0,
			"defense"			: 1,
			"magic defense"		: 1,
			"fire resistance"	: 2,
			"ice resistance"	: 2,
			"speed"				: 1.5
		}

		self.statistics_base = {
			"health"		: 120 +  (25 * difficulty),
			"attack"		: 125 +  (15 * difficulty),
			"endurance"		: 100 +  (20 * difficulty),
			"vitality"		: 80  +  (8 * difficulty),
			"mana"			: 100 +  (4 * difficulty),
			"movement speed": 135 +  (20 * difficulty),
			"intellect"		: 100 +  (5 * difficulty)
		}


		for key in self.statistics_base:
			self.statistics_base[key] = (self.statistics_base[key]
									* (self.level_modifier[key] ** level))
		self.current_health = self.statistics_base["health"]
		self.current_mana = self.statistics_base["mana"]

		self.inventory = list()
		self.inventory.append(Weapon.FireAndIceCrossBows(2,10,True))

		self.drops = {
			"experience" 	: 100 * level,
			"gold"			: 90 * level,
			"items"			: self.inventory
		}

TYPES = {
	"goblin" : Goblin,
	"dragon" : Dragon
}