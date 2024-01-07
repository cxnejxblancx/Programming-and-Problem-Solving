# 40% chance available ladder
# ladder can be random size from [1, 100] meters tall

# import random
import random

# input
ladder_dist_from_wall = float(input("How many meters from the wall will the ladder be? "))
wall_height = float(input("How many meteers tall is the wall? "))

# calculations
ladder_min_height = (((wall_height ** 2) + (ladder_dist_from_wall ** 2)) ** 1/2)

# randomly generate
random_availability = random.randint(1, 100)
random_ladder_height = random.randint(1, 100)

# check if ladder is available based on 40% chance and if of sufficient height
ladder_is_available = (random_availability > 60) # greater than 60 indicates 40% chance of availability
ladder_right_height = (random_availability >= ladder_min_height)

can_reach_roof = ((ladder_right_height) and (ladder_is_available))

# print
print("From a distance of " + str(ladder_dist_from_wall) + " meters and a wall height of " + str(wall_height) + " meters, can we reach the roof?: " + str(can_reach_roof))
