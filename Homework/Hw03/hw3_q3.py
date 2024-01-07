# input
num_rows = int(input("Please enter a positive integer: "))

# for-loop --> iterate through rows of box
for row in range(num_rows + 2): # +2 --> rows for top and bottom frame
    # conditionals --> control what is printed in each row based on the current row number
    if (row == 0) or (row == (num_rows + 1)): # if in the first or last row
        # print
        print("+", "+", sep = (("-") * num_rows)) # top and bottom frame structure

    else:
        # variable
        left_border = "|"

        # for-loop
        for col in range((row), 0, -1): # iterate through columns per row
            # concatenate left border with column number
            left_border = (left_border + str(col))

        complete_row = left_border + ((" " * (num_rows - row))) + "|" # add spaces and a "|" to the end of each row
        print(complete_row) # print the completed rows
