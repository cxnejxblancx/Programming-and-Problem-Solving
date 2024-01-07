# import random for probability
from random import randint

# input
num_rows = int(input("Please enter the desired number of rows: "))

# for-loop
for row in range(1, (num_rows + 1)):
    # variable --> empty string
    complete_row = ""

    # probability
    reverse = randint(0, 100)
    
    # conditionals to implement 50% chance of being in reverse order
    if reverse > 50: # 50% change the random number is greater than 50 (51 - 100) inclusive
        for column in range(1, (row + 1)):
            # variables
            product = str(row * column)
            complete_row = ((complete_row) + (product) + ("\t")) # add each product per colums number to the string
        
        # final print
        print(complete_row)

    elif reverse < 50: # 50% change the random number is less than 50 (0 - 49) inclusive
        for column in range((row), 0, -1):
            # variables
            product = str(row * column)
            complete_row = ((complete_row) + (product) + ("\t")) # add each product per colums number to the string
        
        # final print
        print(complete_row)
