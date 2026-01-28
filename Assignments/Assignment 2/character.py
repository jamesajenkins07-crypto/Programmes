#!/bin/python3

'''
FULL NAME: James Jenkins
STUDENT NUMBER: 251491498
UWO USERNAME: jjenki48
CREATION DATE: 2026-01-28
DESCRIPTION: Generates characters for RPG Dungeons & Dragons utilising random module.
'''


from random import randint

# Calculate character traits

total_trait_values = ''
trait_count = 0
max_trait_index = 0
max_trait = 0

for i in range(6):

    trait_value = 0
    total_rolls = ''

# Roll Dice 4x
    for i in range(4):
        roll = randint(1, 6)
        total_rolls += str(roll)

# Determine lowest roll
    lowest_roll = min(total_rolls)

# Sum rolls less lowest
    for number in total_rolls:
        trait_value += int(number)
    trait_value -= int(lowest_roll)

# Determine highest trait
    if trait_value > max_trait:
        max_trait = trait_value
        max_trait_index = trait_count

    if trait_value < 10:
        trait_value = '0' + str(trait_value)
    else:
        trait_value = str(trait_value)

# Add trait to string of all traits
    total_trait_values += trait_value

# Add count for determining place of max trait
    trait_count += 1

# Outline character abilities
charisma = int(total_trait_values[0:2])
constitution = int(total_trait_values[2:4])
dexterity = int(total_trait_values[4:6])
intelligence = int(total_trait_values[6:8])
strength = int(total_trait_values[8:10])
wisdom = int(total_trait_values[10:12])

# Determine max trait bonus
if max_trait == 18:
    bonus = "+4"
if 16 <= max_trait <= 17:
    bonus = "+3"
if 14 <= max_trait <= 15:
    bonus = "+2"
if 12 <= max_trait <= 13:
    bonus = "+1"
if 10 <= max_trait <= 11:
    bonus = "+0"
if 8 <= max_trait <= 9:
    bonus = "-1"
if 6 <= max_trait <= 7:
    bonus = "-2"
if 4 <= max_trait <= 5:
    bonus = "-3"
if max_trait == 3:
    bonus = "-4"

# Determine character class
if max_trait_index == 0:
    character_type = "Sorcerer"
    bonus_trait = "Charisma"
    print("The character's highest ability score is Charisma:", max_trait)
if max_trait_index == 1:
    character_type = "Barbarian"
    bonus_trait = "Constitution"
    print("The character's highest ability score is Constitution:", max_trait)
if max_trait_index == 2:
    character_type = "Rogue"
    bonus_trait = "Dexterity"
    print("The character's highest ability score is Dexterity:", max_trait)
if max_trait_index == 3:
    character_type = "Wizard"
    bonus_trait = "Intelligence"
    print("The character's highest ability score is Intelligence:", max_trait)
if max_trait_index == 4:
    character_type = "Fighter"
    bonus_trait = "Strength"
    print("The character's highest ability score is Strength:", max_trait)
if max_trait_index == 5:
    character_type = "Druid"
    bonus_trait = "Wisdom"
    print("The character's highest ability score is Wisdom:", max_trait)

# Output

print("The recomended character class is:", character_type.upper())
print()
print("The", character_type, "has the following stats:")
print(f"Charisma:        {charisma:2d}")
print(f"Constitution:    {constitution:2d}")
print(f"Dexterity:       {dexterity:2d}")
print(f"Intelligence:    {intelligence:2d}")
print(f"Strength:        {strength:2d}")
print(f"Wisdom:          {wisdom:2d}")
print(f"They get a {bonus} bonus to {bonus_trait}.")
