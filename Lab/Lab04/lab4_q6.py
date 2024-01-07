# import
from random import randrange

# pre-print
print("Welcome to Blackjack!")

# generate random card sum
dealer_card_sum = randrange(2, 22) # [2, 21]
player_card_sum = randrange(1, 12) # [1, 11]

# print
print("Your current card sum is: " + str(player_card_sum))

# ask what they would like to do next
next_step = input("What would you like to do next?: (DEAL, STAND) ")

# while-loop
while (player_card_sum < 21) and (next_step != "STAND"):
    new_card = randrange(1, 12) # [1, 11]
    player_card_sum += new_card
    print("Your current card sum is: " + str(player_card_sum))
    next_step = input("What would you like to do next?: (DEAL, STAND) ")

# conditionals
if (player_card_sum <= 21) and (player_card_sum > dealer_card_sum):
    print("You won! Your card sum was " + str(player_card_sum) + " and the dealer's was " + str(dealer_card_sum))

elif player_card_sum == dealer_card_sum:
    print("You tied! Your card sum was " + str(player_card_sum) + " and the dealer's was " + str(dealer_card_sum))

else:
    print("You lost! Your card sum was " + str(player_card_sum) + " and the dealer's was " + str(dealer_card_sum))
