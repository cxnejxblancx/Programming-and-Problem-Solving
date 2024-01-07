# import randrange
from random import randrange

# inputs
poke_level = int(input("What is this Pokémon's level? "))
poke_speed = int(input("What is this Pokémon's speed? "))

# variables
threshold_value = (poke_speed / 2)
random_value = randrange(0, 256) # [0, 255]

# conditionals
if threshold_value > random_value:
    damage_multiplier = round((((2 * (poke_level)) + 6) / ((poke_level) + 6)), 2)
    print("The Pokémon's move will be " + str(damage_multiplier) + "x stronger!")
    
else:
    print("The Pokémon did not land a critical hit! :(")
  
