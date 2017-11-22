#coding=utf-8

from colors import *
from main import *

def test():
    display("#"*10, pink)
    display("#"*10, blue)
    display("#"*10, green)
    display("#"*10, yellow)
    display("#"*10, red)

    print("")

    display("Random Number: " + str(Random().random(1,6)))
    display("Random Hero: " + Random().name(0))
    display("Random Hostile: " + Random().name(1))
    display("Random Language Set: " + ", ".join(Random.language()))

    w_weapon = Random.weapon(person = "player", c = "Warrior", exp = XP)
    display("Random Warrior Weapon: " + w_weapon.name + ", " + str(w_weapon.damage) + " damage.")

    a_weapon = Random.weapon(person = "player", c = "Assassin", exp = XP)
    display("Random Assassin Weapon: " + a_weapon.name + ", " + str(a_weapon.damage) + " damage.")

    m_spell = Random.weapon(person = "player", c = "Mage", exp = XP)
    display("Random Mage Spell: " + m_spell.name + ", " + str(m_spell.damage) + " damage.")

    hostile = Random.hostile()
    display("Random Hostile: " + hostile.name + ", " + str(hostile.health) + " health, " + hostile.inventory[0].name + " with " + str(hostile.inventory[0].damage) + " damage.")

    r = input()
    
    if r == "b":
        battle()

    elif r == "m":
        me()

if __name__ == "__main__":
    test()

# Notes.

# PINK
# Text used to show data/instructions.

# BLUE
# Text used to narrate.

# GREEN
# Text used by Gerald, the AI.

# YELLOW
# Text for names of friendlies.

# RED
# Text for names of hostiles.

# CLASSES
# Inside Unnamed, there will be four classes.
#
# WARRIOR
# -- Heroic – uses melee weapons.

# MAGE
# -- Uses magic and wit to defeat enemies.

#

# TYPES
# Types should be represented as the following numbers:
# -- Hero/Player => 0
# -- Hostile => 1
# -- Friendly => 2
# -- Province => 3
# -- Place => 4

# PROVINCE
# A province is a area of land, like a district name or town name. For example, "Akulu" is a provine or region, whereas
# "The Western Inn" would be a place.

# PLACE
# A place is a place in a province or region, such as "The Riverside School"

# ------
