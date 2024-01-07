# import
import random

# generate random number
rand_num = random.randint(0, 100)

# determine if number even / greater than 50
is_even = (rand_num % 2 == 0)
is_greater_than_50 = (rand_num > 50)

# print
print(str(rand_num) + " is even: " + str(is_even))
print(str(rand_num) + " is greater than 50: " + str(is_greater_than_50))
