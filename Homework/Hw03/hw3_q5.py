# import randrange to give the player their cards
from random import randrange

# input
will_play = input("Would you like to play 'Twenty-One'? [y/n] ")

# while-loop (play the game?)
while (will_play != 'y') and (will_play != 'n'):
    will_play = input("Would you like to play 'Twenty-One'? [y/n] ")

# conditionals
if will_play == 'n':
    print("Thank you for playing!")

else: # if will_play == 'y'
    # variables
    card1 = randrange(1, 12) # [1, 11]
    card2 = randrange(1, 12) # [1, 11]
    user_score = ((card1) + (card2))
    opponent_score = randrange(0, 101) # [0, 100]

    # while-loop (opponent score)
    while (opponent_score < 3) or (opponent_score > 33): # ensure score between 3 and 33
        opponent_score = randrange(0, 101)

    # print
    print("Your cards are worth " + str(card1) + " and " + str(card2) + ".")

    # input
    will_continue = input("Would you like another card? [y/n] ")

    # conditionals
    if user_score != 21:
        # while-loop (invalid input)
        while (will_continue != 'y') and (will_continue != 'n'):
            will_continue = input("Would you like another card? [y/n] ")

        # conditional
        if will_continue == 'y':
            new_card = randrange(1, 12) # [1, 11]
            user_score += new_card

        # print
        print("Your score is " + str(user_score) + "!")
        print("Your opponent's score is " + str(opponent_score) + "!")

        # conditionals
        if user_score > 21:
            if opponent_score > 21:
                print("It's a draw!")

            else: # if opponent_score =< 21
                print("Your opponent wins! Their score was " + str(opponent_score) + ".")

        else: # if user_score < 21 because user_score already != 21
            if opponent_score > 21:
                print("You win! Your score was " + str(user_score) + ".")

            elif opponent_score == 21:
                print("Your opponent wins! Their score was " + str(opponent_score) + ".")

            else: # if opponent_score < 21
                if (21 - user_score) < (21 - opponent_score):
                    print("You win! Your score was " + str(user_score) + ".")

                elif (21 - opponent_score) < (21 - user_score):
                    print("Your opponent wins! Their score was " + str(opponent_score) + ".")

                else: # if user_score == opponent_score
                    print("It's a draw!")

    else: # if user_score == 21
        if opponent_score != 21:
            print("You win! Your score was " + str(user_score) + ".")

        else: # if opponent_score == 21
            print("It's a draw!")
          
