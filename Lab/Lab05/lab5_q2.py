# input
will_continue = input("Please ENTER to calculate a product or Q to quit: ")

# while-loop
while will_continue != '' and will_continue != 'Q':
    will_continue = input("Please ENTER to calculate a product or Q to quit: ")

# while-loop
while will_continue == '':
    # variables
    first_factor = int(input("Please input your first factor: "))
    second_factor = int(input("Please input your second factor: "))
    
    # conditionals
    if first_factor <= 0 or second_factor <= 0:
        print("ERROR: Positive integers must be entered.")

    else:
        product = first_factor * second_factor
        print("Your product is: " + str(product))

    # input
    will_continue = input("Please ENTER to calculate a product or Q to quit: ")
