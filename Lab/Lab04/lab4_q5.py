# input
num_values = int(input("Please enter how many positive values you want to consider: "))

# variable
largest_value = 0

# pre-print
print("Enter your values:")

# for-loop
for i in range(num_values):
    # input
    user_value = float(input(""))

    # conditonal
    if user_value > largest_value:
        largest_value = user_value

    # adjust variable
    i += 1

# final print
print("The largest of these values is " + str(largest_value))
