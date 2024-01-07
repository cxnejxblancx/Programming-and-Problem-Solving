# input
lower_string = input("Please enter a string of lowercase letters: ")

# variables
decreasing = True
stop_location = 0

# for loop
for char in range(len(lower_string)):
    if char < (len(lower_string) - 1):
        if lower_string[char] <= lower_string[char + 1]:
            decreasing = False

            if stop_location == 0:
                stop_location = char + 1

# conditionals
if decreasing:
    print(lower_string + " is decreasing.")

else:
    print(lower_string + " is not decreasing.")
    print("It stopped being lexicographically decreasing at location " + str(stop_location))
