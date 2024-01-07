# import
from math import sqrt

# inputs
a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))

# calculations
discriminant = (b ** 2) - (4 * a * c)

# conditionals
if a != 0:
    if discriminant > 0:
        solution1 = ((-b) + sqrt(discriminant)) / (2 * a) # quadratic formula (+)
        solution2 = ((-b) - sqrt(discriminant)) / (2 * a) # quadratic formula (-)
        print("This equation has 2 real solutions: x = " + str(solution1) + ", x = " + str(solution2))

    elif discriminant == 0:
        only_solution = ((-b) / 2 * a)
        print("This equation has 1 real solution: x = " + str(only_solution))

    else: # discriminant < 0
        print("This equation has no real solution.")

else:
    if (b == 0) and (c == 0):
        print("This equation has infinite solutions.")
      
    elif (b == 0) and (c != 0):
        print("This equation has no solution.")
