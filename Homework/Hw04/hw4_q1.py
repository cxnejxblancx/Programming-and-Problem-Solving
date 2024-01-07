# input
base = float(input("Please enter a positive integer to serve as the base: "))

# while-loop --> ensure user ensures positive, non-zero, whole number values
while base <= 0 or base % 1 != 0:
    base = float(input("Invalid value for the base (" + str(base) + "). Please enter a positive integer to serve as the base: "))

# adjust correct base
base = int(base)

# separate
print()

# input continued...
highest_power = float(input("Please enter a positive integer to sever as the highest power: "))

# while-loop --> ensure user ensures positive, non-zero, whole number values
while highest_power <= 0 or highest_power % 1 != 0:
    highest_power = float(input("Invalid value for the highest power (" + str(highest_power) + "). Please enter a positive integer to serve as the highest power: "))

# adjust correct highest power
highest_power = int(highest_power)

# separate
print()

# for-loop
for num in range((highest_power), -1, -1):
    if num % 2 == 0:
        exponential = base ** num
        print(str(base) + " ^ " + str(int(num)) + " = " + str(exponential))
