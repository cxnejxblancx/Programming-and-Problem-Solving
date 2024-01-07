# input
user_string = input("Say something: ")

# variables
lower_string = ""
num_changed = 0
num_unchanged = 0
num_whitespace = 0 # ' ' and '\n'
num_nonalpha = 0

#for-loop
for char in range(len(user_string)):
    if (user_string[char] == ' ') or (user_string[char] == '\n'): # check for whitespace characters --> also non-alpha charcters
        num_whitespace += 1
        num_nonalpha += 1
        lower_string += user_string[char]

    elif 97 <= ord(user_string[char]) <= 122: # check for unchanged lowercase letters
        num_unchanged += 1
        lower_string += user_string[char]

    elif 65 <= ord(user_string[char]) <= 90: # check for changed uppercase letters
        num_changed += 1
        lower_from_upper = chr(ord(user_string[char]) + 32) # 32 accounts for difference between uppercase and lowercase ascii values
        lower_string += lower_from_upper

    else: # check for other characters
        num_nonalpha += 1
        lower_string += user_string[char]

# final prints
print(lower_string)
print("Number of changed letters: " + str(num_changed))
print("Number of unchanged letters: " + str(num_unchanged))
print("Number of whitespace characters: " + str(num_whitespace))
print("Number of non-alphabetic characters: " + str(num_nonalpha))
