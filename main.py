#coding=utf-8

import sys, os, random, time, math, pygame
from colors import *
from tests import *

# Global Variables.
CLASS = ""
RANDOM_STRINGS = []
LANGUAGE = []
HELP_TIMES = 0
XP = 0
PLAYER = None
GOD_BOOL = False
# -----------------


pygame.mixer.init()
pygame.mixer.set_num_channels(64)

def play(sound, volume = 0.25, indef = False):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play( -1 if indef else 1 )

def stop():
    pygame.mixer.stop()
    pygame.mixer.music.stop()

def correct():
    play("sounds/effects/General Sounds/Pause Sounds/sfx_sounds_pause4_in.wav", 0.03)

def incorrect():
    play("sounds/effects/General Sounds/Negative Sounds/sfx_sounds_error4.wav", 0.03)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Spell:
    def __init__(self, name, base_damage, level):
        self.name = name
        self.damage = base_damage * level

class Character:
    def __init__(self, name, t, health, inventory, exp):
        self.name = name
        self.type = t
        self.health = health
        self.inventory = inventory
        self.exp = exp


class Warrior(Character):
    def __init__(self, n):
        super().__init__(
            name = n,
            t = "Warrior",
            health = 100,
            inventory = [],
            exp = 0
        )

class Mage(Character):
    def __init__(self, n):
        super().__init__(
            name = n,
            t = "Mage",
            health = 80,
            inventory = [],
            exp = 0
        )

class Assassin(Character):
    def __init__(self, n):
        super().__init__(
            name = n,
            t = "Assassin",
            health = 70,
            inventory = [],
            exp = 0
        )

class Hostile(Character):
    def __init__(self, n, h, i):
        super().__init__(
            name = n,
            t = "Hostile",
            health = h,
            inventory = i,
            exp = 5
        )


class Random:
    @classmethod
    def random(self, a,b):
        return random.randint(a,b)

    @classmethod
    def language(self, vowels = ["a", "e", "i", "o", "u"], consonants = ["p", "t", "k", "m", "n", "s", "l"], silibants = ["s"],
                 liquids = ["r", "l"], finals = ["m", "n"], s_length = 20):

        syllables = []

        while len(syllables) <= 10:
            # We're using the "(optional silibant) consonant vowel final" structure.
            roll = self.random(1, 2)

            if roll == 1:
                syllables.append(random.choice(silibants) + random.choice(consonants) + random.choice(vowels) + random.choice(finals) )

            elif roll == 2:
                syllables.append(random.choice(consonants) + random.choice(vowels) + random.choice(finals))

            else:
                print("A random value out of 1 or 2 just gave us a different value. Why???!!")
                return

        return syllables

    @classmethod
    def word(self, word_length = [2,3]):
        roll = self.random(word_length[0], word_length[1])

        curr = ""
        for _ in range(roll):
            curr += random.choice(LANGUAGE)

        return curr

    @classmethod
    def name(self, t):
        if t == 0:
            names = ["Achilles", "Alec", "Ajax", "Alexander", "Atlas", "Blaine", "Beowulf", "Bolivar", "Balthasor", "Frederic",
                     "Gable", "Gage", "Gabe", "Graydon", "Godric", "Hades", "Hercules", "Hunter", "Ives", "Julius", "Kade", "Kaelan",
                     "Khronos", "Luther", "Maximus", "Maxamillion", "Osias", "Perseus", "Saxon", "Tiberius"]

            adjective = ["Bold", "Courageous", "Daring", "Epic", "Fearless", "Gallant", "Grand", "Gusty", "Noble", "Valiant", "Elevated",
                         "Dauntless", "Lion-Hearted", "Unafraid", "Valorous"]

            curr = random.choice(names) + " The " + random.choice(adjective)

            if curr in RANDOM_STRINGS:
                return Random.name(0)
            else:
                RANDOM_STRINGS.append(curr)
                return curr

        if t == 1:
            names = ["Kade", "Kaelan", "Khronos", "Luther", "Maximus", "Maxamillion", "Osias", "Perseus", "Saxon", "Tiberius", "Ash",
                     "Bates", "Beast", "Bones", "Bram", "Casper", "Chucky", "Crow", "Damien", "Dexter", "Draco", "Edgar", "Freddy", "Gomez",
                     "Hannibal", "Jack", "Lucifer", "Norman", "Poe", "Pugsley", "Rasputin", "Romero", "Salem", "Spike", "Storm", "Thorn", "Vlad"]

            adjective = ["Bad", "Corrupt", "Destructive", "Hateful", "Heinous", "Hideous", "Malevolent", "Malicious", "Nefarious",
                         "Ugly", "Unpleasant", "Vicious", "Villainous", "Wiked", "Foul", "Beastly", "Baneful", "Calamitous", "Harmful",
                         "Wrathful"]


            curr = random.choice(names) + " The " + random.choice(adjective)

            if curr in RANDOM_STRINGS:
                return Random.name(1)
            else:
                RANDOM_STRINGS.append(curr)
                return curr

        if t == 2:
            names = ["Chloe", "Emily", "Aaliyah", "Emma", "Olivia", "Jennifer", "Hannah", "Kellie", "Jessica", "Lauren", "Sarah", "Lily",
                     "Ava", "Mia", "Jasmine", "Isabella", "Sophia", "Grace", "Ella", "Rebecca", "Charlotte", "Abigail", "Amy", "Aaron",
                     "Jacob", "Shawn", "Michael", "Daniel", "Alex", "Ryan", "James", "David", "Mattew", "Jack", "Muhammad", "Alexander",
                     "Jordan", "Kevin", "Dylan", "Christopher", "Chris", "Blake", "Joshua", "Adam", "Robert", "Joseph", "William", "George"]

            noun = ["Accountant", "Taxer", "Farmer", "Blacksmith", "Alchemist", "Librarian", "Brickmaker", "Lawyer", "Apprecntice", "Priest",
                    "Dentist", "Doctor", "Barber", "Merchant", "Nurse", "Musician", "Pharmacists", "Pirate", "Guard", "Servant", "Stonemason",
                    "Traveler", "Brewer", "Butcher", "Carpenter"]


            curr = random.choice(names) + " The " + random.choice(noun)

            if curr in RANDOM_STRINGS:
                return Random.name(2)
            else:
                RANDOM_STRINGS.append(curr)
                return curr

        if t == 3:
            place_types = ["Tavern", "Inn"]
            # TODO: ["Tavern", "Inn", "Bank", "Market Place", "Hall", "Butchers", "Factory", "Centre", "Castle" ]
            curr = random.choice(place_types)

            if curr == "Tavern":
                structure = ["The", "", "Tavern"]
                adjective = ["Dusty", "Quiet", "Ancient", "Bustling", "Crowded", "Drunkard", "Sleepy", "Irish", "Welsh", "Dirty", "Stuffy",
                             "Mucky", "Golden", "Nimble", "Laughing", "Goofy", "Chunky", "Warm", "Olde", "Familiar", "Naughty", "Faded"]

                structure[1] = random.choice(adjective)
                curr = " ".join(structure)

            elif curr == "Inn":
                structure = ["The", "", "Inn"]
                adjective = ["Dusty", "Quiet", "Ancient", "Bustling", "Crowded", "Drunkard", "Sleepy", "Irish", "Welsh", "Dirty", "Stuffy",
                             "Mucky", "Golden", "Nimble", "Laughing", "Goofy", "Chunky", "Warm", "Olde", "Familiar", "Naughty", "Faded"]

                structure[1] = random.choice(adjective)
                curr = " ".join(structure)

    @classmethod
    def weapon(self, c, person = "player", exp = XP):
        if person == "player":
            if c == "Warrior":
                weapons = ["Axe", "Longsword", "Mace", "Sword", "Gauntlets"]
                xp = math.floor(exp/15)

                if xp == 0:
                    adjectives = ["Rusty", "Wooden", "Broken", "Busted", "Collapsed", "Cracked", "Crushed", "Mutilated", "Ruptured",
                                  "Shattered", "Smashed"]

                    damage = self.random(2,3) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 1:
                    adjectives = ["Brittle", "Stone", "Weak", "Beginner", "Amateur", "Dusty", "Cracked", "Damaged", "Fractured", "Beat-Up"]

                    damage = self.random(3,4) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 2:
                    adjectives = ["Iron", "Scratched", "Strong", "Repaired"]

                    damage = self.random(4,5) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 3:
                    adjectives = ["Steel", "Strong", "Tough", "Solid", "Firm", "Hardy"]

                    damage = self.random(5,6) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 4:
                    adjectives = ["Robust", "Mighty", "Strapping", "Fibrous", "Sturdy"]

                    damage = self.random(6,7) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 5:
                    adjectives = ["Brilliant", "Intense", "Dazzling", "Stimulating", "Shining"]

                    damage = self.random(7, 8) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 6:
                    adjectives = ["Exquisite", "Charming", "Elegant", "Impeccable", "Precise"]

                    damage = self.random(8, 9) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 7:
                    weapons = ["The Ethereal Sword Of Sun", "The Celestial Axe Of The New Dawn", "The Sublime Mace Of New Life",
                                "The Ghostly Gauntlets Of The Second Moon"]

                    damage = self.random(10,11) * 10
                    curr = random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

            elif c == "Assassin":
                weapons = ["Dagger", "Knife", "Shank", "Blade", "Nunchucks"]
                xp = math.floor(exp/15)

                if xp == 0:
                    adjectives = ["Rusty", "Wooden", "Broken", "Busted", "Collapsed", "Cracked", "Crushed", "Mutilated", "Ruptured",
                                  "Shattered", "Smashed"]

                    damage = self.random(2,8) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 1:
                    adjectives = ["Brittle", "Stone", "Weak", "Beginner", "Amateur", "Dusty", "Cracked", "Damaged", "Fractured", "Beat-Up"]

                    damage = self.random(8,16) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 2:
                    adjectives = ["Iron", "Scratched", "Strong", "Repaired"]

                    damage = self.random(16,24) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 3:
                    adjectives = ["Steel", "Strong", "Tough", "Solid", "Firm", "Hardy"]

                    damage = self.random(24,32) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 4:
                    adjectives = ["Robust", "Mighty", "Strapping", "Fibrous", "Sturdy"]

                    damage = self.random(32,40) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 5:
                    adjectives = ["Brilliant", "Intense", "Dazzling", "Stimulating", "Shining"]

                    damage = self.random(40, 48) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 6:
                    adjectives = ["Exquisite", "Charming", "Elegant", "Impeccable", "Precise"]

                    damage = self.random(60, 70) * 10
                    curr = random.choice(adjectives) + " " + random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

                if xp == 7:
                    weapons = ["The Concealed Dagger Of The Third Sun", "The Ethereal Kinfe Of Ancient Souls", "The Glowing Shank Of The 8th Star",
                               "The Vanishing Blade Of Wartime", "The Swift Nunchucks Of Light"]

                    damage = self.random(70, 90) * 10
                    curr = random.choice(weapons)

                    if curr in RANDOM_STRINGS:
                        return Random.weapon(person, c)

                    return Weapon(curr, damage)

            elif c == "Mage":
                spells = ["Frost Spike", "Frostfire Wrath", "Blackout", "Elemental Blaze", "Blackout", "Purge Sould", "Hymn of Spirits", "Distortion Blast",
                          "Lunar Arrow", "Soul Torrent", "Fire Flood", "Deluge", "Assualt of the Void", "Decay Flash", "Thuder Nova", "Arcane Orb", "Shadow Form",
                          "Mutation of Frost", "Holy Fury", "Monsoon", "Rage of Light", "Air Explosion", "Elemental Whip", "Unholy Eruption", "Shooting Star",
                          "Burst of Light", "Purity of Death", "Mutation of Honesty", "Calm of Shadows", "Arcane Blaze", "Void Bolt", "Hellfire",
                          "Eclipse", "Flare of the Moon", "Assault of Demonic Anger", "Resurrection of Blessings", "Obliteration Wave", "Rain of Despair"]

                curr = random.choice(spells)
                damage = self.random(2, 3) * 10

                if curr in RANDOM_STRINGS:
                    return Random.weapon(person, c)

                return Spell(curr, damage, math.ceil((exp + 1)/15))


    @classmethod
    def hostile(self, exp = XP):
        level = math.floor(float(exp)/float(15))

        if level == 0:
            hostiles = ["Goblin", "Orc", "Evil Leprechaun", "Troll"]
            return Hostile(n = random.choice(hostiles), h = self.random(8, 10) * 10, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 1:
            hostiles = ["Goblin", "Orc", "Evil Leprechaun", "Troll", "Werewolf"]
            return Hostile(n = random.choice(hostiles), h = self.random(10, 18) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 2:
            hostiles = ["Goblin", "Orc", "Evil Leprechaun", "Troll", "Werewolf", "Demon"]
            return Hostile(n = random.choice(hostiles), h = self.random(18, 26) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 3:
            hostiles = ["Goblin", "Orc", "Evil Leprechaun", "Troll", "Werewolf", "Demon", "Ghost", "Griffin"]
            return Hostile(n = random.choice(hostiles), h = self.random(26, 34) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 4:
            hostiles = ["Goblin", "Orc", "Evil Leprechaun", "Troll", "Werewolf", "Demon", "Ghost", "Griffin", "Dragon", "Bogeyman", "Evil Unicorn"]
            return Hostile(n = random.choice(hostiles), h = self.random(34, 42) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 5:
            # You now start fighting other adventurers.
            return Hostile(n = self.name(1), h = self.random(42, 50) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 6:
            return Hostile(n = self.name(1), h = self.random(50, 58) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])

        if level == 7:
            return Hostile(n = self.name(1), h = self.random(58, 66) * 7, i = [self.weapon(c = "Warrior", person = "player", exp = exp)])


# Global Language Can Now Be Set.
LANGUAGE = Random.language()
# -------------------------------

def run(cmd):
    os.system(cmd)

def compute_rank(xp):
    xp = math.floor(xp/15)

    if xp == 0:
        return "Poop"

    if xp == 1:
        return "Meh"

    if xp == 2:
        return "Huh"

    if xp == 3:
        return "Ok"

    if xp == 4:
        return "Mmmm"

    if xp == 5:
        return "Wow"

    if xp == 6:
        return "Damn"

    if xp == 7:
        return "Geez"

def wait(s):
    time.sleep(s)

def sprompt():
    display(">>> ", pink, "")

    print(pink, end = "")
    result = input()
    print(end)

    return result

def gerald(speech, e = "\r\n"):
    display(speech, green, e)

def help_table():
    print("")
    display("-----------------------------------------------------------------------------------------------------------------------------------------------------------------", pink)
    display("|      Command     |       Function                                                                                                                             |", pink)
    display("| help             | Displays this table. It doesn't go through the entire intro thing again because that would be boring.                                      |", pink)
    display("| me               | Displays all the data about you. (Inventory, XP, Name, Stats...)                                                                           |", pink)
    display("| exit             | Exit the prompt.                                                                                                                           |", pink)
    display("| exec <command>   | Execute the command you type. Please don't, or you could like cheat or something. And cheating is bad. Don't cheat. Please.                |", pink)
    display("| test             | Tests that everything is running smoothly. Stuff like functions and shizzel. You can run it if you want, but it's incredibly underwhelming |", pink)
    display("-----------------------------------------------------------------------------------------------------------------------------------------------------------------", pink)
    print("")


first_run = True
def prompt(enter = False):
    global first_run
    answers = []
    answers.append(sprompt())

    if answers[-1] == "help" and first_run:
        gerald("Hello there. I'm Gerald, your personal (f)artificial inteligence for the entire game. I say fartificial because")
        gerald("I'm actually really, really dumb (a bunch of if statements). You don't belive me? Let's demonstrate this. Please ask")
        gerald("me to do something.")

        demonstrate = sprompt()

        if demonstrate == "":
            gerald("Well you're lazy aren't you...")
            wait(0.5)
            print(" ")

        else:
            gerald("Ok, ok... I might be able to do something with that... Let me think...")
            wait(1.5)
            gerald("...")
            wait(1.5)
            gerald("...")
            wait(1.5)
            gerald("...")
            wait(2.5)

        print("")

        gerald("Anyway, moving onwards: (this entire game will full of rubbish jokes like that)")

        gerald("However, there are a few things I can do. These are all listed in a handy table down here:")
        first_run = False
        help_table()

    elif answers[-1] == "help":
        help_table()
        promt(enter)

    elif answers[-1].split(" ")[0] == "exec":
        exec(" ".join(answers[-1].split(" ").pop(0)))

    elif answers[-1] == "test":
        test()
        prompt(enter)

    elif answers[-1] == "me":
        me()
        prompt(enter)

    elif answers[-1] == "exit":
        return


    elif answers[-1] == "" and not enter:
        prompt(enter)

    elif answers[-1] == "" and enter:
        return answers[-1]

    else:
        return answers[-1]

def narrate(s, w = False, e = "\r\n"):
    display(s, blue, end = e)

    if w == True:
        wait((60/250) * len( s.split(" ") ))

def info(s, w = False, e = "\r\r"):
    display(s, pink, end = e)

    if w == True:
        wait((60/250) * len( s.split(" ") ))


def battle(hostile = Random.hostile(), reward = 5, place = Random.name(3)):
    global PLAYER
    global XP

    max_health = math.ceil(hostile.health/10)
    max_player_health = math.ceil(PLAYER.health/10)

    answers = []


    while not (PLAYER.health <= 0 or hostile.health <= 0):
        while True:

            run("clear")
            gerald("Battle with '" + hostile.name + "' at '" + place + "':")

            print("")

            display(hostile.name + ":", red)
            gerald("-- Weapon: ", e = "")
            info(hostile.inventory[0].name + ", does " + str(hostile.inventory[0].damage/10) + " damage.")

            gerald("-- Health: ", "")

            display("♥"*math.ceil(hostile.health/10) + "_"*(max_health - math.ceil(hostile.health/10)) + " (" + str((hostile.health/10)) + " health)", red)

            print("")

            display(PLAYER.name + " (you):", yellow)
            if PLAYER.type == "Warrior" or PLAYER.type == "Assassin":
                display("-- Inventory: ", green)

                if len(PLAYER.inventory) == 0:
                    display("You currently have no weapons. \n", pink)

                else:
                    for i in range(len(PLAYER.inventory)):
                        weapon = PLAYER.inventory[i]
                        display("---- Name: ", green, "")
                        display(weapon.name + " ", pink, "")
                        display("[" + str(i+1) + "]", green)

                        display("     Damage: ", green, "")
                        display(str(weapon.damage/10) + " health points", pink, "\r\n\n")

            else:
                display("Spell Book: ", green)

                if len(PLAYER.inventory) == 0:
                    display("You currently have no spells. \n", pink)

                else:
                    for i in range(len(PLAYER.inventory)):
                        spell = PLAYER.inventory[i]
                        display("---- Name: ", green, "")
                        display(spell.name + " ", pink, "")
                        display("[" + str(i+1) + "]", green)

                        display("     Damage: ", green, "")
                        display(str(spell.damage/10) + " health points", pink, "\r\n")
                        print("")

            print("")

            display("-- Health: ", green, "")
            display("♥"*math.ceil(PLAYER.health/10) + "_"*(max_player_health - math.ceil(PLAYER.health/10)) + " (" + str(PLAYER.health/10) + " health)", red)

            print("\n")

            gerald("To fight, type 'fight <weapon number> <times to perform>'.", e = "")
            info(" (attacks with high times to perform will most likely fail)")

            gerald("To use a round to heal, type 'heal'.")
            gerald("To pass, type 'pass'.")
            print("")

            heal_amount = Random.random(5,15)

            answers.append(prompt(True))

            if answers[-1].split(" ")[0] == "fight" and len(answers[-1].split(" ")) > 1:
                index = int(" ".join(answers[-1].split(" ")[1])) - 1
                times = math.floor(1 if len((answers[-1].split(" "))) != 3 else int(" ".join(answers[-1].split(" ")[2])))

                weapon = PLAYER.inventory[index]

                chance_of_fail = 2**times
                num = Random.random(1, 10)

                if num > chance_of_fail and not index > len(PLAYER.inventory):
                    hostile.health -= times * PLAYER.inventory[index].damage
                    play("sounds/effects/Weapons/Melee/sfx_wpn_punch1.wav") if (PLAYER.type == "Warrior" or PLAYER.type == "Assassin") else play("sounds/effects/Weapons/Grenade Whistles/sfx_wpn_missilelaunch.wav")
                    print("")
                    gerald("The " + str(times) + " " + ("hit" if times == 1 else "hits") + " with '" + PLAYER.inventory[index].name + "' was succesfull!")
                    break

                elif index > len(PLAYER.inventory):
                    gerald("I'm sorry, thats not an index.")
                    incorrect()

                else:
                    print("")
                    display("The " + str(times) + " " + ("hit" if times == 1 else "hits") + " with '" + PLAYER.inventory[index].name + "' failed!", red)
                    play("sounds/effects/General Sounds/Negative Sounds/sfx_sounds_error3.wav")
                    break


            elif answers[-1] == "heal":
                if PLAYER.health + heal_amount > max_player_health and not PLAYER.health == max_player_health:
                    gerald("Ok, you healed " + str(max_player_health - (PLAYER.health/10)) + " points.")
                    play("sounds/effects/General Sounds/Positive Sounds/sfx_sounds_powerup10.wav")
                    PLAYER.health = max_player_health * 10
                    break

                elif PLAYER.health/10 == max_player_health:
                    gerald("You already have max health, so that move was considered a pass.")
                    incorrect()
                    break

                else:
                    PLAYER.health += heal_amount*10
                    play("sounds/effects/General Sounds/Positive Sounds/sfx_sounds_powerup10.wav")
                    break

            elif answers[-1] == "pass":
                gerald("Ok, waiting for their move.")
                break

            elif answers[-1] == "win":
                gerald("CHEATER!")
                hostile.health = 0
                break

            else:
                display("Oops, you can't do that. Try again.", red)
                incorrect()

        print("")

        if hostile.health <= 0:
            play(
                "sounds/effects/Death Screams/Human/sfx_deathscream_human" + random.choice(["1","2","3","4","5"]) + ".wav"
            )

            info("You won the battle against '" + hostile.name + "'. Press <ENTER> to continue.", e = "")
            input()

            play("sounds/effects/General Sounds/Fanfares/sfx_sounds_fanfare3.wav")

            print("")

            gerald("You won:")
            display("-- Weapon" + ("s" if len(hostile.inventory) > 1 else "") + ": ", green)

            if len(hostile.inventory) == 0:
                display("Something went very wrong. The hostile has no weapons.\n", pink)

            else:
                for i in range(len(hostile.inventory)):
                    weapon = hostile.inventory[i]
                    display("---- Name: ", green, "")
                    display(weapon.name + " ", pink, "")
                    display("[" + str(i+1) + "]", green)

                    display("     Damage: ", green, "")
                    display(str(weapon.damage/10) + " health points", pink, "\r\n\n")

                    PLAYER.inventory.append(hostile.inventory[i])

            XP += reward
            print("")
            gerald("-- Experince: " + str(reward) + "xp ", e = "")
            info("(" + str(15 - (XP % 15)) + " xp to the next level)")

            return [PLAYER, True]

        # Other Turn
        wait(1)

        percentage = (1/max_health) * (hostile.health/10)
        chance_of_heal = 0

        if percentage > 1:
            print("The percentage is above 100%. What has life come to?")

        elif percentage < 0.2:
            chance_of_heal = 7

        elif percentage < 0.5:
            chance_of_heal = 5

        elif percentage < 0.8:
            chance_of_heal = 2


        chance_num = Random.random(1, 10)

        hostile_heal_amount = Random.random(5, 7)

        if chance_num > chance_of_heal or hostile.health == max_health:
            # Attack
            PLAYER.health -= hostile.inventory[0].damage
            display(hostile.name, red, "")
            gerald(" attacked you for " + str(hostile.inventory[0].damage/10) + " damage.")
            play("sounds/effects/General Sounds/Negative Sounds/sfx_sounds_damage3.wav")

        elif hostile.health/10 + hostile_heal_amount > max_health:
            hostile.health = max_health*10

        else:
            # Heal
            hostile.health += hostile_heal_amount * 10
            display(hostile.name, red, "")
            gerald(" healed themselves " + str(hostile_heal_amount) + " health points.")
            play("sounds/effects/General Sounds/Neutral Sounds/sfx_sound_neutral5.wav")

        if PLAYER.health <= 0:
            info("You lost the battle to '" + hostile.name + "'. Press <ENTER> to continue.", e = "")
            play("sounds/effects/General Sounds/Negative Sounds/sfx_sounds_negative1.wav")
            input()

            return [hostile, False]

        info("\nPress <ENTER> to continue.", e = "")
        input()


def me():
    global PLAYER
    global XP

    print("")

    display("Name: ", green, "")
    display(PLAYER.name, pink)

    display("Class: ", green, "")
    display(PLAYER.type, pink)

    display("Health: ", green, "")
    health = math.ceil(PLAYER.health/10)
    max_health = 0

    if PLAYER.type == "Warrior":
        max_health = 10

    elif PLAYER.type == "Mage":
        max_health = 8

    elif PLAYER.type == "Assassin":
        max_health = 7

    display("♥"*health + "_"*(max_health - health), red)
    display("XP: ", green, "")
    display("•"*math.floor(XP/15), yellow, "")
    info(" (" + str((15 - (XP % 15))) + " xp to next level)")

    print("")

    if PLAYER.type == "Warrior" or PLAYER.type == "Assassin":
        display("Inventory: ", green)

        if len(PLAYER.inventory) == 0:
            display("You currently have no weapons. \n", pink)

        else:
            for weapon in PLAYER.inventory:
                display("-- Name: ", green, "")
                display(weapon.name, pink)

                display("   Damage: ", green, "")
                display(str(weapon.damage/10) + " health points", pink, "\r\n\n")

    else:
        display("Spell Book: ", green)

        if len(PLAYER.inventory) == 0:
            display("You currently have no spells. \n", pink)

        else:
            for spell in PLAYER.inventory:
                display("-- Name: ", green, "")
                display(spell.name, pink)

                display("   Damage: ", green, "")
                display(str(spell.damage/10) + " health points", pink, "\r\n")
                print("")

    print("")

def main():
    global PLAYER
    global XP

    randoms = random.sample(range(0, 20), 6)
    battles = []

    for i in range(3):
        battles.append([Random.hostile(), Random.name(3), 5, False])

    while not (battles[0][3] == True and battles[1][3] == True and battles[2][3] == True):
        run("clear")

        if XP % 15 == 0 and XP != 0:
            main()

        gerald("Places: ")
        display("-- Training Dojo ", red, "")
        display("[T]", pink)

        print("")

        gerald("Battles: ")

        for i in range(len(battles)):
            b = battles[i]

            display("-- " + b[1] + ",", red, "")
            display(" with " + b[0].name, yellow, "")
            display(" – reward " + str(b[2]) + " xp. ", green,  end = "")
            display(("X " if b[3] == False else "✓ "), (red if b[3] == False else green), "")
            display("[" + str(i + 1) + "]", pink)

        print("")

        display("Name: ", green, "")
        display(PLAYER.name, pink)

        display("Class: ", green, "")
        display(PLAYER.type, pink)

        display("Health: ", green, "")
        health = math.ceil(PLAYER.health/10)
        max_health = 0

        if PLAYER.type == "Warrior":
            max_health = 10

        elif PLAYER.type == "Mage":
            max_health = 8

        elif PLAYER.type == "Assassin":
            max_health = 7

        display("♥"*health + "_"*(max_health - health), red)
        display("XP: ", green, "")
        display("•"*math.floor(XP/5), yellow, "")
        info(" (" + str((15 - (XP % 15))) + " xp to next level)")

        print("")

        if PLAYER.type == "Warrior" or PLAYER.type == "Assassin":
            display("Inventory: ", green)

            if len(PLAYER.inventory) == 0:
                display("You currently have no weapons. \n", pink)

            else:
                for weapon in PLAYER.inventory:
                    display("-- Name: ", green, "")
                    display(weapon.name, pink)

                    display("   Damage: ", green, "")
                    display(str(weapon.damage/10) + " health points", pink, "\r\n\n")
                    print("")

        else:
            display("Spell Book: ", green)

            if len(PLAYER.inventory) == 0:
                display("You currently have no spells. \n", pink)

            else:
                for spell in PLAYER.inventory:
                    display("-- Name: ", green, "")
                    display(spell.name, pink)

                    display("   Damage: ", green, "")
                    display(str(spell.damage/10) + " health points", pink, "\r\n")
                    print("")

        print("")

        answers = []

        gerald("To access a specific battle, type 'battle <battle number>'.")
        gerald("To use the training dogo, type 'go T'.")
        print("")

        answers.append(prompt())

        if answers[-1].split(" ")[0] == "battle" and len(answers[-1].split(" ")) >= 1:
            i = int(answers[-1].split(" ")[1]) - 1
            result = battle(battles[i][0], battles[i][2], battles[i][1])

            if battles[i][3] == True:
                gerald("That battle has already been completed.", "")
                input()

            else:
                if result[1] == True:
                    print("")
                    gerald("Well done!", "")
                    input()
                    battles[i][3] = True

                else:
                    print("")
                    gerald("Too bad... you can always try again later. ", "")
                    input()

        else:
            gerald("I'm sorry, that is not a command.", "")
            input()



def main_intro():
    global PLAYER

    answers = []
    run("clear")
    narrate("Untitled.", e = "")

    if GOD_BOOL:
        info(" – God Mode Enabled. ")

    else:
        info("")

    narrate("You're on the floor in a deserted opening in the middle of a woodland. Your back hurts, and a terrible pain runs through your legs. ", e = "")
    input()
    correct()

    name = ""
    gerald("Please choose a name (leave blank for a random name)")
    name = prompt(True)
    correct()

    if name == "":
        name = Random.name(0)

    gerald("Please choose a class.")
    gerald("----------------------\n")
    display("Warrior – Uses weapons and brute force to get what they want.", yellow)
    display("-- Health: 100", yellow)
    display("-- Weapon Type: Melee", yellow)

    print("")

    display("Mage – Uses magic and spells to attack enemies", yellow)
    display("-- Health: 80", yellow)
    display("-- Weapon Type: Spells", yellow)
    display("-- Notes: However, using spells zaps a small amount of your health. (A number between one and twenty", yellow)

    print("")

    display("Assassin – Sneaks up on enemies to get them when they're least expecting it", yellow)
    display("-- Health: 70", yellow)
    display("-- Weapon Type: Melee", yellow)

    print("")

    while True:
        answers.append(prompt(True).lower())
        correct()

        if answers[-1] == "warrior" or answers[-1] == "w":
            PLAYER = Warrior(n = name)
            correct()
            break

        elif answers[-1] == "mage" or answers[-1] == "m":
            PLAYER = Mage(n = name)
            correct()
            break

        elif answers[-1] == "assassin" or answers[-1] == "a":
            PLAYER = Assassin(n = name)
            correct()
            break

        else:
            incorrect()
            gerald("I'm afraid that's not a class. Please try again.")

    me()

    input()

    narrate("As you collect your senses, you notice a " + ("spellbook" if PLAYER.type == "Mage" else "weapon") + " on the grass. ", e = "")
    input()
    correct()

    narrate("Out of curiousity, you walk over to it and " + ("read it. " if PLAYER.type == "Mage" else "pick it up. ") , e = "")
    input()
    correct()

    if GOD_BOOL:
        PLAYER.inventory.append( Random.weapon(c = PLAYER.type, person = "player", exp = 7*15) )

    else:
        PLAYER.inventory.append( Random.weapon(c = PLAYER.type, person = "player", exp = XP) )

    gerald("Cool! You just got your first item. You can view its stats by typing 'me' into the prompt.")

    prompt(True)
    correct()

    narrate("Out of the corner of your eye, you spot a shadowy figure. ", e = "")
    input()
    correct()

    gerald("Ok, this is going to be your first battle. ", e = "")
    input()
    correct()

    winners = []
    winners.append(battle(place = "The Forest Opening", reward = 0))

    if winners[-1][1] == True:
        run("clear")
        gerald("You just won your first battle! Well done! ", "")
        input()
        correct()

    elif winners[-1][1] == False:
        run("clear")
        gerald("You just lost your first battle. Geez... you're so bad. You can practice in the ", "")
        info("training dojo", "")
        gerald("later. ", "")
        input()
        correct()

    info("As you recover yourself, you pull out the map located in your rucksack.", "")
    input()

    main()
    main()
    main()
    main()
    main()
    main()
    main()






def intro():
    global GOD_BOOL

    run("clear")

    answers = []
    narrate("Hello, and welcome to Untitled. Untitled is a text adventure game where you go round fighting baddies. Yep, it's really that bad. (Press <ENTER> to continue or type 'skip' to skip) ", e = "")
    answers.append(input())
    correct()

    if answers[-1] == "skip" or answers[-1] == "s":
        main_intro()
    elif answers[-1] == "god" or answers[-1] == "g":
        GOD_BOOL = True
        main_intro()

    else:
        narrate("Now for a quick tutorial. The thing below this text is the prompt, and where you enter your commands for the entire game. (Press <ENTER> to continue)")
        prompt(True)
        correct()

        narrate("You can type 'help' at any time to get a list of commands you can perform. (Press <ENTER> to continue)")
        prompt(True)
        correct()

        narrate("Shall we start? (Y/n)")
        result = prompt(True).lower()
        correct()

        if result == "" or result == "y" or result == "yes":
            main_intro()

        else:
            return

if __name__ == "__main__":
    intro()
