# probablility = math.floor( (max_health * 255 * 4) / (current_health * ball_value) )

# import
    # import randrange
from random import randrange

    # import floor division or use integer division by 1 (x // 1)
from math import floor

# input
max_health = int(input("Enter the max health of this Pokémon: "))

# generate random value
current_health = randrange(1, (max_health + 1))
ball_value = randrange(1, 256) # [0, 255] inclusive on both ends, no zero division --> (1, 256)
random_comparison = randrange(1, 256) # (0, 255) --> exclusive on both ends --> (1, 256)

# variable
probability = floor((max_health * 255 * 4) / (current_health * ball_value))

# conditionals
if probability >= random_comparison:
    print("You've caught the Pokémon!")
else:
    print("Oh no! The Pokémon broke free!")
