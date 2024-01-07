# input
current_xp = float(input("Enter this user's current XP: "))
current_xp = round(current_xp, 1)

# conditionals
if current_xp > 60 or current_xp < 0:
    print("ERROR: Please enter a valid XP value.")

elif current_xp >= 40:
    print("Level 5 Player (XP: " + str(current_xp) + ")")

elif current_xp >= 30:
    print("Level 4 Player (XP: " + str(current_xp) + ")")

elif current_xp >= 25:
    print("Level 3 Player (XP: " + str(current_xp) + ")")

elif current_xp >= 15:
    print("Level 2 Player (XP: " + str(current_xp) + ")")

else:
    print("Level 1 Player (XP: " + str(current_xp) + ")")
