# input
num_players = int(input("How many players played this round: "))

# variables
winning_player = ""
winning_score = 0

# while-loop
while num_players <= 0:
    num_players = int(input("Invalid input. How many players played this round: "))

# for-loop
for player in range(1, (num_players + 1)):
    # variable
    assets = 0
  
    # input
    property_value = input("Enter the value of a property/asset, or DONE to finish: ")

    # while-loop --> keep asking the player to input the value of their assets until they are DONE
    while property_value != "DONE":
        assets += float(property_value)
        property_value = input("Enter the value of a property/asset, or DONE to finish: ")

    # print
    print("Player " + str(player) + " has " + str(round(assets, 2)) + " dollars.")

    # conditional --> keep track of the winning player and their score
    if assets > winning_score:
        winning_player = str(player)
        winning_score = assets

# final print (2)
print("Congratulations, Player " + winning_player + "! You won with $" + str(winning_score) + "!")
