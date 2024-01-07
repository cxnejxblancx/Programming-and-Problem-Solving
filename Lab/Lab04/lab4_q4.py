# input
base = float(input("Please enter a positive integer to serve as the base: "))
power = float(input("Please enter a positive integer to serve as the highest power: "))

# variable
current_int = 0

# conditionals
if (base % 1 != 0) or (power % 1 != 0) or (base < 0) or (power < 0):
    print("ERROR: Both values must be POSITIVE INTEGERS.")

else:
    # chnage inputs into integers
    base = int(base)
    power = int(power)
    
    # for-loop
    for current_int in range(power + 1):
        result = base ** (current_int)
        print(str(base) + " ^ " + str(current_int) + " = " + str(result))

        # adjust variable
        current_int += 1
  
