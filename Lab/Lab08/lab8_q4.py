# Part A
def numberify(word):
    # variable
    numberified_word = ""
    for char in word:
        # conditionals
        if char == "A":
            numberified_word += "4"

        elif char == "E":
            numberified_word += "4"

        elif char == "I":
            numberified_word += "1"

        elif char == "S":
            numberified_word +=  "5"

        elif char == "T":
            numberified_word += "7"

        elif char == "O":
            numberified_word += "0"

        else:
            numberified_word += char.upper()

    # return
    return numberified_word

# PART B
def main():
    # input
    user_string = input("Please enter a message to numberify: ")

    # variables
    user_string += " "
    user_string = user_string.upper()

    numberified_string = ""
    start = 0

    # for-loop
    for char in range(len(user_string)):
        # if complete word encountered
        if user_string[char] == " ":
            stop = char
            ind_word = user_string[start: char] # store the complete word
            start = char + 1 # new start is one after the last space

            # if the complete word is longer than 3
            if len(ind_word) > 3:
                if stop == len(user_string) - 1:
                    numberified_string += numberify(ind_word)
                else:
                    numberified_string += f"{numberify(ind_word)} "

            else:
                if stop == len(user_string) - 1:
                    numberified_string += ind_word
                else:
                    numberified_string += f"{ind_word} "

    # final prints
    print()
    print(f"Your numberified string is: {numberified_string}")
        
main()
