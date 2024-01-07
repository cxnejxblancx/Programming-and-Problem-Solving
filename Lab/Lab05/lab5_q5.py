# input
width = int(input("Python needs to tell you a secret. How many characters wide can its message be? "))

# variables
indiv_length = width
full_length = width * 3
space_between = width - 2
space_infront = 0

# for-loop
for row in range(1, (full_length + 1)):
        if row <= indiv_length: # or ((indiv_length * 2) < row <= (indiv_length * 3)):
            if row <= ((indiv_length - 1) / 2):
                print((" " * (row - 1)) + "x", "x", sep = (" " * (space_between)))
                space_between -= 2
                space_infront += 1

            elif row == (((indiv_length - 1) / 2) + 1):
                print((" " * (row - 1) + "x"))

            else:
                print(((" " * (space_infront - 1)) + "x"), "x", sep = (" " * (space_between + 2)))
                space_between += 2
                space_infront -= 1

        elif row <= (2 * indiv_length):
            if (row == width + 1) or (row == width * 2):
                print(" " + ("o" * (width - 2)))

            else:
                 print("o", "o", sep = (" " * (width - 2)))

        else: 
            if row <= (full_length - (indiv_length / 2)):
                print((" " * (space_infront)) + "x", "x", sep = (" " * (space_between)))
                space_between -= 2
                space_infront += 1

            elif row == (full_length - ((indiv_length - 1) / 2)):
                print((" " * (space_infront) + "x"))

            else:
                print(((" " * (space_infront - 1)) + "x"), "x", sep = (" " * (space_between + 2)))
                space_between += 2
                space_infront -= 1
             
